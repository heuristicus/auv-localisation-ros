#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
from loc_sonar.msg import proc_sonar, particle_data, point, line
from std_msgs.msg import String
import map_rep, sys, s_math, particle, particle_list

class Localiser:

    def __init__(self):
        self.get_params()
        self.particles = particle_list.ParticleList(self.particle_num)
        self.map = map_rep.MapRep(self.mapfile)
        self.scale = self.map.scale
        self.math = s_math.SonarMath()
        self.create_publishers()
        self.create_subscribers()
        rospy.spin()

    def create_subscribers(self):
        self.actsub = rospy.Subscriber('sonar_pre', proc_sonar, self.update)
        rospy.init_node('localiser')

    def create_publishers(self):
        if self.use_gui:
            self.guipub = rospy.Publisher('particle', particle_data)
            self.updatepub = rospy.Publisher('particle_update', String)
            self.bestpub = rospy.Publisher('best_particle', particle_data)

    def generate_particles(self, loc, angle):
        """Create a number of particles."""
        # the sonar only knows where it is in the first step (let's
        # pretend), and so when you don't know where the sonar is we
        # generate points based on our localised value
        if not loc:
            loc = self.estimated_loc
        if not self.particles.initialised():
            for i in range(self.particles.max_particles()):
                # Create a particle within a gaussian range of the current sonar location
                self.particles.add(particle.Particle(self.math.apply_point_noise(loc.x, loc.y, self.loc_noise, self.loc_noise, pret=True), self.map, self.math.get_noise(angle, self.ang_noise)))

    def weight_particle(self, sonar_ranges, sonar_angle, particle):
        """Weights the given particle according to the difference
        between its ranges and the ranges detected by the sonar."""
        #prang = [r/100 if r != -1 else r for r in particle.ranges] # normalise the measurement to metres to be the same as the sonar data
        for sr, pr in zip(sonar_ranges, particle.ranges):
            print sr, pr
            if bool(sr == -1) ^ bool(pr == -1):
                particle.wt += 0.0001
            else:
                particle.wt += 0.0001 if sr == pr else self.math.gaussian(sr, 5, pr)
        #print particle.wt       
        
    def update(self, data):
        # maybe there should be separate methods which update based on
        # action and sonar range data. This means that the localiser
        # should be able to cope with backlogs in the actions since it
        # will scan through the actions missed and move particles
        # along all vectors that have not been processed yet.
        #if self.use_gui:
            #self.updatepub.publish('update started')
        to_move = data.next
        angle = data.angle
        prev_pos = data.prev
        sonar_ranges = data.ranges
        actual = data.actual

        self.generate_particles(prev_pos, angle) # only if no particles are present in the list
        self.particles.resample_meanvar()
        #self.particles.resample() # only if particles exist and have weights
        #for particle in self.particles.list():
         #   self.guipub.publish(weight=0.2, loc=point(particle.loc.x, particle.loc.y), angle=particle.initial_angle)
        move_vector = self.math.get_move_vector(prev_pos, to_move)
        #print '-------------'
        for particle in self.particles.list():
            particle.move(move_vector, angle)
            particle.get_ranges(self.scale)
            #print particle.ranges
            self.weight_particle(sonar_ranges, angle, particle)
            if self.use_gui:
                mline = particle.move_line.coords
                mv = line(point(mline[0][0], mline[0][1]), point(mline[1][0], mline[1][1]))
                self.guipub.publish(weight=particle.wt, loc=point(particle.loc.x, particle.loc.y), angle=particle.heading, ranges=particle.ranges, moveline=mv, scan=particle.scan)
        #print self.particles.mean
        self.guipub.publish(weight=0.2, loc=point(self.particles.mean[0], self.particles.mean[1]), flag=1)
        best = self.particles.best()

        mline = best.move_line.coords
        mv = line(point(mline[0][0], mline[0][1]), point(mline[1][0], mline[1][1]))
        self.bestpub.publish(weight=best.wt, loc=point(best.loc.x, best.loc.y), angle=best.heading, ranges=best.ranges, moveline=mv, scan=best.scan, flag=2)
        
    def get_localisation_error(self):
        lsa = self.particles.best().loc
        return (self.loc.x - lsa.x, self.loc.y - lsa.y)
    
    def get_location_diff(self, sonar, particle):
        x = abs(sonar.x - particle.x)
        y = abs(sonar.y - particle.y)
        return x + y

    def get_params(self):
        """Reads parameters from a file and saves them in a dictionary"""
        self.max_range = rospy.get_param('sonar_maxrange')
        self.min_range = rospy.get_param('sonar_minrange')
        self.angle_range = rospy.get_param('sweep_angle')
        self.step = rospy.get_param('sonar_step')
        self.ang_noise = rospy.get_param('angle_noise')
        self.loc_noise = rospy.get_param('location_noise')
        self.rng_noise = rospy.get_param('range_noise')
        self.mapfile = rospy.get_param('loc_map')
        self.particle_num = rospy.get_param('particle_num')
        self.use_gui = rospy.get_param('use_gui')

if __name__ == '__main__':
    Localiser()
