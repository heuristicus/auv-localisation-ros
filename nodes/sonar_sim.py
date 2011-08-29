#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy, s_math, map_rep, move_list
from loc_sonar.msg import proc_sonar, point

class Sonar:

    def __init__(self, out_file=None):
        self.get_params()
        self.ranges = [] # Distances to objects in the map on previous pulse
        self.scan_lines = []
        self.intersection_points = []
        #self.move_list = move_list # tuples containing a point location and angle of the sonar.
        self.scan_number = self.angle_range/self.step
        self.map = map_rep.MapRep(fname=self.map_file) # Map to use the sonar in
        self.scale = self.map.scale
        self.move_list = move_list.MoveList(fname=self.move_file)
        start_point = self.move_list.first()
        self.start_loc = start_point[0] # Starting location of the sonar in the map
        self.loc = self.start_loc # Current location of the sonar in the map
        self.math = s_math.SonarMath()
        self.set_heading(start_point[1])
        self.file = out_file
        self.make_pub()
        self.run_sim()

    def get_params(self):
        """Reads parameters from a file and saves them in a dictionary"""
        self.max_range = rospy.get_param('sonar_maxrange')
        self.min_range = rospy.get_param('sonar_minrange')
        self.step = rospy.get_param('sonar_step')
        self.ang_noise = rospy.get_param('angle_noise')
        self.loc_noise = rospy.get_param('location_noise')
        self.rng_noise = rospy.get_param('range_noise')
        self.angle_range = rospy.get_param('sweep_angle')
        self.move_file = rospy.get_param('move_list')
        self.map_file = rospy.get_param('loc_map')

    def set_heading(self, angle):
        """Sets the heading to the angle given, and then changes the
        starting angle of the sonar scan to reflect this change. The
        current setup makes half of the sweep on the left side of the
        heading angle, and the other half on the right of the heading
        angle."""
        self.heading = angle
        hms = self.heading - (self.angle_range/2)
        self.scan_start_angle = hms if hms > 0 else 360 - abs(hms)
        #print self.heading
        print 'head'
        self.head_line = self.math.convert_line(self.math.get_scan_line(self.math.make_point(self.loc.x, self.loc.y), self.heading + 90, 40))

    def reset(self):
        self.ranges = []
        self.scan_lines = []
        self.intersection_points = []
        
    def make_pub(self):
        self.out = rospy.Publisher('sonar_pre', proc_sonar)
        rospy.init_node('sonar_sim')

    def move_to_random(self, height, width):
        """Moves the sonar to a random position within a height x
        width rectangle."""
        self.move_to(Point(random.randint(0, width), random.randint(0, height)), random.randint(0,360))

    def move_to_random_bounded(self, height, width, bound):
        """Moves to a random location within a height x width
        rectangle, but within a bounded range of its current
        location"""
        self.move_to(Point(random.randint(self.loc.x - bound, self.loc.x + bound), random.randint(self.loc.y - bound, self.loc.y + bound)), random.randint(self.initial_angle - bound, self.initial_angle - bound))

    def run_sim(self):
        while self.move_list.get_next() is not -1:
            self.sim_step()
            rospy.sleep(1) # pretend actions take some time

    def sim_step(self):
        prev = self.loc
        nextmv = self.move_list.next()
        next = nextmv[0]
        angle = nextmv[1]
       
        move_vector = self.math.get_move_vector(prev, next)
        if move_vector is not(0,0):
            angle_noise = self.math.get_noise(0, self.ang_noise)
            #angle_noise = 0
            endpt = self.math.rotate_point(prev, move_vector, angle_noise)
            n_end = self.math.apply_point_noise(endpt.x, endpt.y, self.loc_noise, self.loc_noise, pret=True)

            ###### MAY CAUSE ERRORS #######

            # might be good to set this so that a value is added or
            # subtracted from this, so that the uncertainty of your
            # current bearing are taken into account.
            # subtracting this value from 315 gives an approximate of 0 to north
            #print self.initial_angle, 'SONARb', angle
            #self.initial_angle = 315 - printangle + angle_noise
            #self.initial_angle = angle + angle_noise
            #print self.initial_angle, 'SONARa', angle
            #self.initial_angle = 0
            
            ###### MAY CAUSE ERRORS #######

            self.loc = n_end
            self.set_heading(angle + angle_noise)
        #else:
        #    self.set_heading(angle)
        self.get_ranges()
        self.ranges = [r/100 for r in self.ranges]
        self.out.publish(prev=point(prev.x, prev.y), next=point(next.x, next.y), angle=angle, ranges=self.ranges, actual=point(self.loc.x, self.loc.y), scan=self.scan_lines, head_line=self.head_line)
        
    def get_ranges(self):
        """Get the ranges that the sonar would receive at its current
        map position if its sensors were perfect."""
        self.reset() # reset arrays containing scan lines, ranges etc. 
        #a = []
        current_angle = self.scan_start_angle
        for i in range(self.scan_number): # loop over the total number of measurements to take
            #a.append(self.current_angle)
            # get the line from the sonar to the point of max range
            ln = self.math.get_scan_line(self.loc, current_angle, self.max_range)
            # get the intersection point with the scan line on the map
            # that is closest to the current sonar location
            intersect = self.math.get_intersect_point(self.loc, ln, self.map)
            # calculate the distance to the intersection point, with
            # some parameters which limit the data to a certain range
            dist = self.math.intersect_distance(self.loc, intersect, self.min_range, self.max_range)
            self.ranges.append(dist) # store the calculated distance
            # Store the other objects for drawing later if necessary
            self.scan_lines.append(self.math.convert_line(ln))
            self.intersection_points.append(intersect)
            current_angle += self.step # increment the angle to the angle of the next measurement
        #print map(int, a)

if __name__ == '__main__':
    Sonar()
