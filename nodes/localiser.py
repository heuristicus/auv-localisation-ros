#!/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
from loc_sonar.msg import sonar_action
import map_rep, gui, sys, move_list, s_math, particle, particle_list, sonar

class Localiser:

    def __init__(self, particle_num, mapfile, sonar_params, paramfile=''):
        self.particles = particle_list.ParticleList(particle_num)
        self.map = map_rep.MapRep(fname=mapfile)
        self.read_noise_params(fname=paramfile)
        self.math = s_math.SonarMath()
        if sonar_params['type'] is not 'hw':
            sonar_params['map_'] = mapfile
            self.sonar = sonar.Sonar(**sonar_params)

        self.create_subscribers()

    def create_subscribers(self):
        self.actsub = rospy.Subscriber('sonar_action', sonar_action, self.update)
        self.init_node('localiser')

    def generate_particles(self):
        """Create a number of particles."""
        sonar_loc = self.sonar.loc()
        # the sonar only knows where it is in the first step (let's
        # pretend), and so when you don't know where the sonar is we
        # generate points based on our localised value
        if not sonarloc:
            sonarloc = self.estimated_loc
        if not self.particles.initialised():
            for i in range(self.particles.max_particles()):
                # Create a particle within a gaussian range of the current sonar location
                self.particles.add(particle.Particle(Point(self.math.apply_point_noise(self.sonar.x, self.sonar.y, self.loc_noise, self.loc_noise)), self))

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

        self.generate_particles(self.num_particles) # only if no particles are present in the list
        self.particles.resample() # only if particles exist and have weights
        move_vector = self.math.get_move_vector(prev_pos, to_move)
        for particle in self.particles.list():
            particle.move(move_vector, angle)
            particle.get_ranges(self.scale)
            self.weight_particle(particle)

        # print self.get_localisation_error()
        
    def get_localisation_error(self):
        lsa = self.particles.best().loc
        return (self.loc.x - lsa.x, self.loc.y - lsa.y)

    def read_noise_params(self, fname):
        """Reads parameters from a file and saves them in a dictionary"""
        if not fname:
            self.ang_noise = 5
            self.loc_noise = 0.5
            self.rng_noise = 0.5
        else:
            f = open(fname)
            s = f.read().split('\n')[:-1]
            params = {}
            for param in s:
                z = param.split(' = ')
                params[z[0]] = float(z[1])
            self.ang_noise = params.get('ang_ns')
            self.loc_noise = params.get('loc_ns')
            self.rng_noise = params.get('rng_ns')

if __name__ == '__main__':
    s_param = {'max_rng':50, 'step': 15, 'move_list': 'i.mv'}
    s_param = {'type': 'hw'}
    l = Localiser(25, 'gisbert.map', s_param, paramfile='params.txt')
