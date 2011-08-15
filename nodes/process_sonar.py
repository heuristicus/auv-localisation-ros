#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy

from loc_sonar.msg import sonar_return
from std_msgs.msg import String

global return_arr

def newdata(sonar):
    """
    
    Arguments:
    - `sonar`:
    """
    ind = int(round(sonar.beardeg))
    return_arr[ind].append(ind) # put ranges in here

def update(val):
    global x, y, rng
    x = rospy.get_param('sonar/x')
    y = rospy.get_param('sonar/y')
    rng = rospy.get_param('sonar/rng')
    print x,y,rng

def get_distance(bins):
    """
    """
    threshold = 150
    blanking_dist = 0.3
    
    bin_rng = rng/len(bins)
    


def main():
    """
    """
    global sub
    global return_arr
    return_arr = [[] for x in range(360)]
    rospy.init_node('process_sonar')
    sub = rospy.Subscriber('sonar_info', sonar_return, newdata)
    sub = rospy.Subscriber('param_update', String, update)
    rospy.spin()
    
if __name__ == '__main__':
    main()
