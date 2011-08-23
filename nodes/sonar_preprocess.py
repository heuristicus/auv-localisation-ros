#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
from loc_sonar.msg import sonar_struct, proc_sonar


def initialise():
    create_subscribers()
    create_publishers()
    get_params()

def pre_real(data):
    print 'processing real data'
    ## The data coming in here will be raw data containing bins and so on, which will need to be processed accordingly.

def pre_sim(data):
    print 'processing sim data'
    action.publish(data)

def create_subscribers():
    global real, sim
    real = rospy.Subscriber('sonar_readable', sonar_struct, pre_real)
    sim = rospy.Subscriber('sonar_sim_readable', proc_sonar, pre_sim) 
    rospy.init_node('sonar_preprocess')

def create_publishers():
    global action
    action = rospy.Publisher('sonar_pre', proc_sonar)

def get_params():
    global angle_range, step
    angle_range = rospy.get_param('sweep_angle')
    step = rospy.get_param('sonar_step')

if __name__ == '__main__':
    initialise()
    rospy.spin()
