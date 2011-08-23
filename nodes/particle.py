#!/usr/bin/python
import s_math
from shapely.geometry import Point

class Particle:
    

    #### Need to fix the initialisation - do not rely on sonar. when
    #### copying the particle take the values that the particle has,
    #### not the current sonar parameters.
    def __init__(self, loc, sonar, wt=0):
        self.loc = loc
        self.sonar = sonar
        self.wt = wt
        self.scan = []
        self.int = []
        self.map = sonar.map
        self.maxrange = sonar.max_range
        self.minrange = sonar.min_range
        self.initial_angle = sonar.initial_angle
        self.current_angle = self.initial_angle
        self.angle_range = sonar.angle_range
        self.step = sonar.step
        self.scan_number = self.angle_range/self.step
        self.math = s_math.SonarMath()
        self.move_line = None

    def get_ranges(self, scale):
        self.scan = []
        self.int = []
        self.current_angle = self.initial_angle
        self.ranges = []
        for i in range(self.scan_number):
            ln = self.math.get_scan_line(self.loc, self.current_angle, self.maxrange)
            intersect = self.math.get_intersect_point(self.loc, ln, self.map)
            dist = self.math.intersect_distance(self.loc, intersect, self.minrange, self.maxrange,)
            dist = dist/scale # normalise the distance
            self.scan.append(ln)
            self.int.append(intersect)
            self.ranges.append(dist)
            self.current_angle += self.step
        self.math.apply_range_noise(self.ranges, self.sonar.rng_noise)

    def move(self, vector, angle):
        """Move the particle along a vector, and set its scan start angle. Introduces noise."""
        angle_noise = self.math.get_noise(0, self.sonar.ang_noise)
        # Rotate endpoint of the vector by the noisy angle
        endpt = self.math.rotate_point(self.loc, vector, angle_noise)
        # Apply noise to the endpoint location
        n_end = Point(self.math.apply_point_noise(endpt.x, endpt.y, self.sonar.loc_noise, self.sonar.loc_noise))
        self.initial_angle = angle + angle_noise
        
        last = self.loc
        self.loc = n_end
        self.move_line = self.math.make_line(last, self.loc)

    def copy(self):
        return Particle(self.loc, self.sonar)
        
        
