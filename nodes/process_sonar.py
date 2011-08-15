#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy

from loc_sonar.msg import sonar_return

global return_arr

def newdata(sonar):
    """
    
    Arguments:
    - `sonar`:
    """
    ind = int(round(sonar.beardeg))
    return_arr[ind].append(ind) # put ranges in here

def get_distance(bins):
    """
    """
    threshold = 150
    blanking_dist = 0.3
    
    bin_rng = pulse_range/len(bins)
    


def main():
    """
    """
    global sub
    global return_arr
    return_arr = [[] for x in range(360)]
    rospy.init_node('process_sonar')
    sub = rospy.Subscriber('sonar_info', sonar_return, newdata)
    rospy.spin()
    
if __name__ == '__main__':
    main()
