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
    # angles at which particles are scanning
    sd = get_scan_data(0)
    rng = []
    for i in range(sd[1]):
        ang = (sd[0] + (i * step))%360 # angle of the scan we want
        print ang
        rng.append(data.ranges[ang] if data.ranges[ang] != 0 else -1)
    print rng
    data.angle = 90 # the angle on the simulator at 0 is facing east, in the experiments the sonar was facing zero degrees in its frame, which is 90 in the particles' reference frame
    action.publish(data)

def create_subscribers():
    global real, sim
    real = rospy.Subscriber('sonar_readable', sonar_struct, pre_real)
    sim = rospy.Subscriber('sonar_sim_readable', proc_sonar, pre_sim) 
    rospy.init_node('sonar_preprocess')

def create_publishers():
    global action
    action = rospy.Publisher('sonar_pre', proc_sonar)

def get_scan_data(heading):
    hma = heading - (angle_range/2)
    s_start = hma if hma > 0 else 360 - abs(hma)
    num_scans = angle_range/step
    return (s_start, num_scans)

def get_params():
    global angle_range, step
    angle_range = rospy.get_param('sweep_angle')
    step = rospy.get_param('sonar_step')

if __name__ == '__main__':
    initialise()
    rospy.spin()
