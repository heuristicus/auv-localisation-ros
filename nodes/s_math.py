#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
from loc_sonar.msg import line, point
from math import sin, radians, cos, e, pi, sqrt, degrees, acos, atan2
from shapely import *
from shapely.geometry import LineString, Point
import sys, random

class SonarMath:

    def get_intersect_point(self, location, scan_line, map_):
        """Get the closest intersection point betweena scan line and a line which makes up the map to a location """
        x = []
        for line in map_.lines:
            x.append(scan_line.intersection(line))
        min_dist = sys.maxint
        closest = None
        for c in x:
            cur_dist = c.distance(location)
            if cur_dist < min_dist:
                min_dist = cur_dist
                closest = c
        return closest
    
    def intersect_distance(self, location, intersect, minrange, maxrange):
        if not intersect:
            return -1
        else:
            dist = intersect.distance(location)
            if minrange < dist < maxrange:
                return dist
            else:
                # Distance not in tolerated range so return an 'error' reading.
                return -1

    def get_scan_line(self, location, angle, length):
        """Get a line between a central point and a point on a circle of radius length centred on the location, where the line is rotated by the given angle"""
        pt = self.point_at_angle(location, angle, length)
        ln = LineString([location.coords[0], pt.coords[0]])
        return ln

    def convert_line(self, ln):
        c = ln.coords
        return line(point(c[0][0], c[0][1]), point(c[1][0], c[1][1]))
       
    def point_at_angle(self, centre, degrees, radius):
        """Get the point at a given angle on a circle. The zero degree heading is facing east."""
        # (x', y') = (x + r cos a, y + r sin a)
        # x,y = centre point, r = radius, a = angle
        return Point(centre.x + (radius * cos(radians(degrees))), centre.y + (radius * sin(radians(degrees))))

    def angle_at_pt(self, point, centre):
        """Calculates the angle of a point on a circle"""
        radius = self.pt_dist(point, centre)
        p0 = self.make_point(centre.x + radius, centre.y) # point at zero degrees (facing east)
        ptd = self.pt_dist(point, p0)
        gam = acos(((2*pow(radius, 2)) - pow(ptd, 2))/(2*pow(radius, 2))) # law of cosines
        return degrees(gam)

    def angle_at_pt2(self, point, centre):
        """Calculates the angle of a point on a circle"""
        radius = self.pt_dist(point, centre)
        p0 = self.make_point(centre.x, centre.y - radius)
        a = 2 * atan2(point.x - p0.x, point.y - p0.y)
        return a

    def apply_range_noise(self, lst, sigma):
        """Apply gaussian noise to all values in a list of ranges"""
        noise_ranges = []
        for i in lst:
            # only apply noise if the value is not an error value
            noise_ranges.append(random.gauss(i,sigma) if i != -1 else -1)
        return noise_ranges

    def apply_point_noise(self, x, y, xsigma, ysigma, pret=False):
        """Apply gaussian noise to a point"""
        x = random.gauss(x, xsigma)
        y = random.gauss(y, ysigma)
        if pret:
            return Point(x,y)
        return (x,y)

    def get_noise(self, value, sigma):
        """Get some gaussian noise"""
        return random.gauss(value, sigma)

    def get_move_vector(self, p1, p2):
        """Get a vector that represents the movement from p1 to p2"""
        return (p2.x - p1.x, p2.y - p1.y)

    def rotate_point(self, centre, vector, angle):
        """Rotates the point at the end of the vector from the centre
        point by a given angle around the given rotation centre."""
        sn = sin(radians(angle))
        cs = cos(radians(angle))
        pt = (centre.x + vector[0], centre.y + vector[1])
        x = pt[0]*cs - pt[1]*sn + centre.x + centre.y*sn - centre.x*cs
        y = pt[0]*sn + pt[1]*cs + centre.y - centre.x*sn - centre.y*cs
        return Point(x,y)

    def gaussian(self, mu, sigma, x):
        """Get the probability of the value x on a gaussian"""
        p1 = 1/(sqrt(2*pi*pow(sigma,2)))
        p2 = pow(e, ((-1*pow((x-mu),2)))/(2.0*pow(sigma,2)))
        return p1*p2

    def make_line(self, p1, p2, tp='lnstr'):
        """Make a line between the two points."""
        if tp == 'lnstr':
            try:
                return LineString([(p1.x, p1.y),(p2.x, p2.y)])
            except AttributeError:
                return LineString([(p1[0], p1[1]),(p2[0], p2[1])])
        elif tp == 'ros':
            try:
                return line(point(p1.x, p1.y), point(p2.x, p2.y))
            except AttributeError:
                return line(point(p1[0], p1[1]), point(p2[0], p2[1]))

    def make_lines(self, pt_list):
        return map(self.make_line, pt_list[:-1], pt_list[1:])

    def make_point(self, x, y):
        return Point(x, y)

    def pt_dist(self, p1, p2):
        try:
            return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2))
        except AttributeError:
            return sqrt(pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2))

    def calc_loc_mean_variance(self, point_list, weight_list):
        x = [point.x for point in point_list]
        y = [point.y for point in point_list]
        #print weight_list
        xmv = self.calc_mean_variance(x, weight_list)
        ymv = self.calc_mean_variance(y, weight_list)
        return [xmv, ymv]

    def calc_mean_variance(self, val_list, weight_list):
        wsum = sum(weight_list)
        mean = self.calc_mean(val_list, weight_list)
        var = self.calc_var(val_list, weight_list, mean)
        return (mean, var)

    def calc_mean(self, val_list, weight_list):
        mean = 0
        for val, wt in zip(val_list, weight_list):
            mean += wt * val
        return mean / sum(weight_list)
    
    def calc_var(self, val_list, weight_list, mean):
        var = 0
        for val, wt in zip(val_list, weight_list):
            var += pow(wt * (val - mean), 2)
        return var / sum(weight_list)

if __name__ == '__main__':
    a = SonarMath()
    for i in range(100):
        print a.point_at_angle(Point(0,0), 0, 40)
    #a.rotate_vector(Point(20,8), (40,80), -30)
    #print a.get_move_vector(Point(10,10), Point(5,5))
    #print a.gaussian(356.34777832,5,356.138794019)
    #print a.normpdf(356.34777832,5,356.138794019)
    #print a.calc_mean_variance([5,6,7,1,2,3], [0.1,0.4,0.7,0.9,0.3,0.6])
