#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
import sys
import serial
import time
import numpy
from std_msgs.msg import String

# Import required data types
from loc_sonar import sonar

def sonarTalker():
    print "Sending new parameters"
    pub.publish(LLim=3200,RLim=3200)

   
if __name__ == '__main__':
    rospy.init_node('sonar_updateParams')
    pub = rospy.Publisher('sonar_update', sonar)
    time.sleep(0.25)
    #while not rospy.is_shutdown():
    sonarTalker()
    time.sleep(3)
    #rospy.spin()
