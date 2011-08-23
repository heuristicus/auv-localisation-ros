#!/usr/bin/python

class Sonar:

    def __init__(self, map_, move_list, max_rng=50, min_rng=4, step=25, out_file=None, param_file=None):
        self.read_params(param_file)
        self.ranges = [] # Distances to objects in the map on previous pulse
        self.scan_lines = []
        self.intersection_points = []
        #self.move_list = move_list # tuples containing a point location and angle of the sonar.
        self.max_range = max_rng # Maximum range of the sonar pulse in cm
        self.min_range = min_rng
        self.step = step # Angle moved by the sonar head between each pulse
        self.angle_range = 270 # Total angle that the sonar sweeps through
        self.scan_number = self.angle_range/self.step
        # Where the first pulse is directed from. Sonar initialised so
        # that the first pulse travels from -125, where up is 0.
        self.map = map_ # Map to use the sonar in
        self.scale = self.map.scale

        start_point = move_list.first()
        self.start_loc = start_point # Starting location of the sonar in the map
        self.loc = self.start_loc # Current location of the sonar in the map
        self.initial_angle = start_point[1]
        self.current_angle = self.initial_angle
        self.file = out_file
        self.math = s_math.SonarMath()

    def read_params(self, fname):
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
                                        
    def reset(self):
        self.ranges = []
        self.scan_lines = []
        self.intersection_points = []
        self.current_angle = self.initial_angle

    def move_to_noisy(self, vector, rotation):
        """Moves the sonar to the next point, with noise applied to
        the angle and point."""
        if self.first:
            self.move_to(vector, rotation)
            self.first = False
        else:
            angle_noise = self.math.get_noise(0, self.ang_noise)
            endpt = self.math.rotate_point(self.loc, vector, angle_noise)
            self.loc = Point(self.math.apply_point_noise(endpt.x, endpt.y, self.loc_noise, self.loc_noise))
            # apply gaussian noise to the rotation
            self.initial_angle = 315 - rotation + angle_noise

    def move_to_random(self, height, width):
        """Moves the sonar to a random position within a height x
        width rectangle."""
        self.move_to(Point(random.randint(0, width), random.randint(0, height)), random.randint(0,360))

    def move_to_random_bounded(self, height, width, bound):
        """Moves to a random location within a height x width
        rectangle, but within a bounded range of its current
        location"""
        self.move_to(Point(random.randint(self.loc.x - bound, self.loc.x + bound), random.randint(self.loc.y - bound, self.loc.y + bound)), random.randint(self.initial_angle - bound, self.initial_angle - bound))

    def get_ranges(self):
        """Get the ranges that the sonar would receive at its current
        map position if its sensors were perfect."""
        self.reset() # reset arrays containing scan lines, ranges etc. 
        for i in range(self.scan_number): # loop over the total number of measurements to take
            # get the line from the sonar to the point of max range
            ln = self.math.get_scan_line(self.loc, self.current_angle, self.max_range)
            # get the intersection point with the scan line on the map
            # that is closest to the current sonar location
            intersect = self.math.get_intersect_point(self.loc, ln, self.map)
            # calculate the distance to the intersection point, with
            # some parameters which limit the data to a certain range
            dist = self.math.intersect_distance(self.loc, intersect, self.min_range, self.max_range,)
            self.ranges.append(dist) # store the calculated distance
            # Store the other objects for drawing later if necessary
            self.scan_lines.append(ln)
            self.intersection_points.append(intersect)
            self.current_angle += self.step # increment the angle to the angle of the next measurement
