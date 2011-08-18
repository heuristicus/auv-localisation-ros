#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy

from loc_sonar.msg import sonar_return
from std_msgs.msg import String

def newdata(sonar):
    """
    
    Arguments:
    - `sonar`:
    """
    global bin_rng
    bin_rng = float(rng/float(len(sonar.bins)))
    #print bin_rng
    ind = int(round(sonar.beardeg))
    return_arr[ind].append(get_distance(sonar.bins)) # put ranges in here
    
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
    wrk = [x if x > threshold else 0 for x in bins[blank_index:]]
    avg = sum(wrk)/len(wrk)
    return get_first(wrk) * bin_rng

def get_first(arr):
    """Returns the index of the first non-zero element of an array.
    
    Arguments:
    - `arr`:
    """
    for i in range(len(arr)):
        if arr[i] is not 0:
            return i
    return 0

    
def save_array():
    global return_arr, x, y, rng
    if x is 0 or y is 0 or rng is 0:
        return
    else:
        # average of the two ranges if there are for a certain angle
        return_arr = [sum(z)/len(z) if len(z) >= 1 else z for z in return_arr]
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
        cv += '%f '%(val) if val else '%d '%(0)
    return cv[-1]


def main():
    """
    """
    global x, y, rng
    x = 0
    y = 0
    rng = 0
    global info, par, return_arr, threshold, blanking_dist
    return_arr = [[] for x in range(360)]
    threshold = 140
    blanking_dist = 0.3
    info = rospy.Subscriber('sonar_info', sonar_return, newdata)
    par = rospy.Subscriber('param_update', String, update)
    rospy.init_node('process_sonar')
    rospy.spin()
    
if __name__ == '__main__':
    main()
