#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy

from loc_sonar.msg import sonar_struct, point_range
from std_msgs.msg import String, UInt16

def newdata(sonar):
    """
    
    Arguments:
    - `sonar`:
    """
    global bin_rng
    bin_rng = round(float(rng/float(len(sonar.bins))), 3)
    #print bin_rng
    #print sonar.bins
    ind = int(round(sonar.beardeg))
    dist = get_distance(sonar.bins)
    return_arr[ind].append(dist)
    data = point_range()
    data.x = x
    data.y = y
    data.angle = ind
    data.range = round(dist, 3)
    pts.publish(data)
    
def update(val):
    global x, y, rng
    save_array()
    x = rospy.get_param('sonar/x')
    y = rospy.get_param('sonar/y')
    rng = rospy.get_param('sonar/rng')
    rospy.loginfo('Parameter update: x=%d, y=%d, rng=%d'%(x,y,rng))
    
def get_distance(bins):
    """
    """
    blank_index = int(round(blanking_dist/bin_rng))
    #print 'Ignore up to index %d'%(blank_index)
    wrk = [x if x > threshold else -1 for x in bins[blank_index:]]
    avg = sum(wrk)/len(wrk)
    dist = get_first(wrk) * bin_rng
    print dist
    return dist

def get_first(arr):
    """Returns the index of the first non-zero element of an array.
    
    Arguments:
    - `arr`:
    """
    for i in range(len(arr)):
        if arr[i] != 0:
            return i
    return 0

    
def save_array():
    global return_arr, x, y, rng
    if x == 0 or y == 0 or rng == 0:
        return
    else:
        # average of the two ranges if there are for a certain angle
        for i in range(len(return_arr)):
            try:
                if len(return_arr[i]) > 0:
                    return_arr[i] = sum(return_arr[i])/len(return_arr[i])
            except Exception:
                return_arr[i] = 0
        
        f = open('prc_%d_%d_%d.txt'%(x,y,rng), 'w')
        f.write(string_arr(return_arr))
        f.close()
    return_arr = [[] for x in range(360)]

def string_arr(array):
    """
    
    Arguments:
    - `array`:
    """
    cv = ''
    for val in array:
        cv += '%.3f '%(val) if val else '%d '%(0)
    return cv[:-1]


def main():
    """
    """
    global x, y, rng
    x = 0
    y = 0
    rng = 0
    global info, par, pts, return_arr, threshold, blanking_dist
    return_arr = [[] for x in range(360)]
    threshold = 135
    blanking_dist = 0.3
    info = rospy.Subscriber('sonar_readable', sonar_struct, newdata)
    par = rospy.Subscriber('param_update', String, update)
    pts = rospy.Publisher('point_data', point_range)
    rospy.init_node('process_sonar')
    rospy.spin()
    
if __name__ == '__main__':
    main()
