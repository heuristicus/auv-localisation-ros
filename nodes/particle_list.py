#!/usr/bin/python
import random, s_math, particle
from math import sqrt

class ParticleList:
    
    def __init__(self, particle_num):
        self.max_p = particle_num
        self.particles = []
        self.math = s_math.SonarMath()
        self.mean = (0,0)
        
    def add(self, particle):
        if len(self.particles) < self.max_p:
            self.particles.append(particle)
            return True
        else:
            return False
        
    def list(self):
        return self.particles
    
    def initialised(self):
        return True if self.particles else False

    def max_particles(self):
        return self.max_p

    def cur_particles(self):
        return len(self.particles)

    def best(self):
        """Find the particle with the highest weight"""
        m = 0
        best = None
        for p in self.particles:
            if p.wt > m:
                best = p
                m = p.wt
        return best

    def weights(self):
        """Get the weights for all particles in the list"""
        return [p.wt for p in self.particles]

    def locs(self):
        return [p.loc.coords[0] for p in self.particles]

    def angles(self):
        return [p.heading for p in self.particles]

    def resample(self):
        """Resample the particles in the list probabilistically -
        particles with a higher weight have a higher probability of
        being chosen to be duplicated. Any particles not chosen are
        discarded."""
        if not self.particles or sum(self.weights()) == 0:
            return # Make sure this is only performed if you have the data required
        wts = self.weights()
        s = sum(wts) # sum of the weights used to get the multiplier for the random value
        mvr = self.math.calc_loc_mean_variance([x.loc for x in self.particles], self.weights())
        self.mean = (mvr[0][0], mvr[1][0])
        # get a number of random values equal to the number of particles, for which the range is 0 <= random <= sum of weights
        rands = [random.random() * s for i in range(len(self.particles))]
        self.wt_sum = []
        # get a list of values that correspond to the upper bounds for
        # a certain particle's weight.
        for i in range(len(wts)):
            if i == 0:
                self.wt_sum.append(wts[i])
            else:
                self.wt_sum.append(wts[i] + self.wt_sum[i-1])

        # For each of the random values, see which particle's weight
        # range it falls into
        n = map(self.wt_less, rands)
        # Create copies of the particles in the array locations from
        # the above calculation
        self.particles = [self.particles[i].copy() for i in n]
        self.random_sample(*mvr)

    def resample_meanvar(self):
        #if not self.particles or sum(self.weights()) is 0:
        #    return # Make sure this is only performed if you have the data required
        loc = self.math.calc_loc_mean_variance([x.loc for x in self.particles], self.weights())
        angs = [x.heading for x in self.particles]
        awts = [x.ang_wt for x in self.particles]
        ang = self.math.calc_mean_variance(angs, awts)
        self.mean = (loc[0][0], loc[1][0])
        m = self.particles[0].map
        self.particles = []
        for i in range(self.max_p):
            l = self.math.apply_point_noise(loc[0][0], loc[1][0], sqrt(loc[0][1]), sqrt(loc[1][1]), pret=True)
            a = self.math.get_noise(ang[0], sqrt(ang[1]))
            self.particles.append(particle.Particle(l, m, a))
    
    def random_sample(self, means, varis, angmv):
        """means is the mean of the x and y, varis is the variance of
        the same, angmv is the mean and variance of the angle.  This
        method should put a number of random particles somewhere in
        the general area of the actual location of the sonar.
        """
        random_prc = 10
        num = self.math.num_from_prc(len(self.particles), random_prc)
        num = int(num + 1) # At least one particle is randomly sampled. Might not be good
        m = self.particles[0].map
        vr = map(lambda x:sqrt(x)*4, varis)
        for i in range(num):
            r = int(math.random() * len(self.particles))
            x = means[0] - (vr[0]/2) + vr[0] * math.random()
            y = means[1] - (vr[1]/2) + vr[1] * math.random()
            ang = self.math.get_noise(angmv[0], sqrt(angmv[1]))
            n_pt = Particle(self.math.make_point(x, y), m, ang)
            
        
    def wt_less(self, val):
        """Returns the list index of the range that the given value
        falls into."""
        for i in range(len(self.wt_sum)):
            if val < self.wt_sum[i]:
                return i
