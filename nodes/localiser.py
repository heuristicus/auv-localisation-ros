#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
from loc_sonar.msg import proc_sonar
import map_rep, sys, s_math, particle, particle_list, sonar_sim

class Localiser:

    def __init__(self):
        self.get_params()
        self.particles = particle_list.ParticleList(self.particle_num)
        self.map = map_rep.MapRep(self.mapfile)
        self.scale = self.map.scale
        self.math = s_math.SonarMath()
        self.create_subscribers()
        rospy.spin()

    def create_subscribers(self):
        self.actsub = rospy.Subscriber('sonar_pre', proc_sonar, self.update)
        rospy.init_node('localiser')

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

    def weight_particle(self, sonar_ranges, particle):
        """Weights the given particle according to the difference
        between its ranges and the ranges detected by the sonar."""
        prob_sum = 0
        for i in range(len(particle.ranges)):
            # Sonar returns -1 if the range received is not in the
            # tolerated range. In this case, the measurement is not
            # reliable, so only give a small weight increase.
            if sonar_ranges[i] is -1 and particle.ranges[i] is -1:
                prob_sum += 0.03
            else:
                # Calculate the probability of the particle range
                # measurement given that the sonar range measurement
                # might have a certain amount of noise
                prob_sum += self.math.gaussian(sonar_ranges[i], self.rng_noise, particle.ranges[i])
        particle.wt = prob_sum
        return prob_sum

    def update(self, data):
        # maybe there should be separate methods which update based on
        # action and sonar range data. This means that the localiser
        # should be able to cope with backlogs in the actions since it
        # will scan through the actions missed and move particles
        # along all vectors that have not been processed yet.
        to_move = data.next
        angle = data.angle
        prev_pos = data.prev
        sonar_ranges = data.ranges

        self.generate_particles(prev_pos, angle) # only if no particles are present in the list
        self.particles.resample() # only if particles exist and have weights
        move_vector = self.math.get_move_vector(prev_pos, to_move)
        for particle in self.particles.list():
            particle.move(move_vector, angle)
            particle.get_ranges(self.scale)
            self.weight_particle(sonar_ranges, particle)

        # print self.get_localisation_error()
        
    def get_localisation_error(self):
        lsa = self.particles.best().loc
        return (self.loc.x - lsa.x, self.loc.y - lsa.y)

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
        #self.use_sim = rospy.get_param('use_sim')

if __name__ == '__main__':
    Localiser()
