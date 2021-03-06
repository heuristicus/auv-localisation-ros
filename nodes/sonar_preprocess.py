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
    ranges = map(lambda x:x*100, data.ranges)
    print ranges
    #print data.ranges
    rng = []
    #a = []
    ### seems like a rotation of -135 or +225 is needed to get this data to match the actual data in the sonar file after it has been through here. This needs to be fixed somehow. This is when ang = (sd[0] + (i * step))%360 and that data is published.
    for i in range(sd[1]):
        ang = (sd[0] + (i * step) + 225)%360 # angle of the scan we want
        #a.append(ang)
        rng.append(ranges[ang] if ranges[ang] != 0 else -1)
    #print rng
    #print a, 'pre'
    data.ranges = rng
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
