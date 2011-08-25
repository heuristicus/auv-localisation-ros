#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy, s_math

class Particle:
    

    #### Need to fix the initialisation - do not rely on sonar. when
    #### copying the particle take the values that the particle has,
    #### not the current sonar parameters.
    def __init__(self, loc, map_, angle, wt=0.001, ang_wt=0.001):
        self.get_params()
        self.loc = loc
        self.wt = wt
        self.ang_wt = ang_wt
        self.scan = []
        self.int = []
        self.map = map_
        self.initial_angle = angle
        self.current_angle = self.initial_angle
        self.scan_number = self.angle_range/self.step
        self.math = s_math.SonarMath()
        self.move_line = None

    def get_params(self):
        """Reads parameters from a file and saves them in a dictionary"""
        self.max_range = rospy.get_param('sonar_maxrange')
        self.min_range = rospy.get_param('sonar_minrange')      
        self.angle_range = rospy.get_param('sweep_angle')
        self.step = rospy.get_param('sonar_step')
        self.ang_noise = rospy.get_param('angle_noise')
        self.loc_noise = rospy.get_param('location_noise')
        self.rng_noise = rospy.get_param('range_noise')

    def get_ranges(self, scale):
        self.scan = []        
        self.int = []
        self.current_angle = self.initial_angle
        self.ranges = []
        for i in range(self.scan_number):
            ln = self.math.get_scan_line(self.loc, self.current_angle, self.max_range)
            intersect = self.math.get_intersect_point(self.loc, ln, self.map)
            dist = self.math.intersect_distance(self.loc, intersect, self.min_range, self.max_range,)
            dist = dist/scale # normalise the distance
            self.scan.append(self.math.convert_line(ln))
            self.int.append(intersect)
            self.ranges.append(dist)
            self.current_angle += self.step
        self.math.apply_range_noise(self.ranges, self.rng_noise)

    def move(self, vector, angle):
        """Move the particle along a vector, and set its scan start angle. Introduces noise."""
        print angle, 'ptcl'
        if vector is (0,0):
            # don't bother applying changes to the particles if there
            # is no movement during the action.
            return
        angle_noise = self.math.get_noise(0, self.ang_noise)
        # Rotate endpoint of the vector by the noisy angle
        endpt = self.math.rotate_point(self.loc, vector, angle_noise)
        # Apply noise to the endpoint location
        n_end = self.math.apply_point_noise(endpt.x, endpt.y, self.loc_noise, self.loc_noise, pret=True)

        ###### MAY CAUSE ERRORS #######

        # might be good to set this so that a value is added or
        # subtracted from this, so that the uncertainty of your
        # current bearing are taken into account.
        # subtracting this value from 315 gives an approximate of 0 to north
        #self.initial_angle = 315 - angle + angle_noise
        self.initial_angle = 0
        ###### MAY CAUSE ERRORS #######
        
        last = self.loc
        self.loc = n_end
        self.move_line = self.math.make_line(last, self.loc)

    def copy(self):
        return Particle(self.loc, self.map, self.initial_angle)
        
        
