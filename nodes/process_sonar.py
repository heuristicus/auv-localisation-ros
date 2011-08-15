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
    return_arr[ind].append(sonar)

def main():
    """
    """
    global sub
    global return_arr
    return_arr = [[] for x in range(360)]
    rospy.init_node('process_sonar')
    sub = rospy.Subscriber('sonar_info', sonar_return, newdata)
    rospy.spin()
    print return_arr

if __name__ == '__main__':
    main()
