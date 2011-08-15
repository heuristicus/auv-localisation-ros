#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
import sys
import serial
import time
import numpy
from std_msgs.msg import String
from loc_sonar.msg import sonar, compass, sonar_polarRange
from rospy.numpy_msg import numpy_msg

global compass_heading

################################################################
def callback(msgData):    
    ### will need heading info from sub/compass.
    ### blanking distance proportional to transducer head angle/shape of sub.
    
    print "msgData:"
    msgData = numpy.fromstring(msgData.data, dtype=numpy.uint8)    
    pingPwr = headerData = numpy.fromstring(msgData.data[31:-1], dtype=numpy.uint8) 
    pingPwr = msgData[31:-1] 
    
    #TEST LINE:
    #pingPwr = msgData[44:-1] 
    #print pingPwr
    
    
    print pingPwr
    print msgData[28]
    ADInterval = rospy.get_param("/ADInterval")
    GlitchCount = rospy.get_param("/GlitchCount")
    ThresholdCount = GlitchCount-1 # as in SonarPing.m
    
    Threshold = rospy.get_param("/Threshold")
    BlankDist = rospy.get_param("/BlankDist")
    Range = rospy.get_param("/Range")
    NBins = rospy.get_param("/NBins")
    
    BinLength = Range/float(NBins)    
    
    ######################################## Current detection threshold ###########################
    NewThreshold = 150
    NewBlankDist = 0.3 #for sonar testing in tank minus vehicle
    ################################################################################################
    
    StartBin = int(numpy.ceil(NewBlankDist/BinLength))
    
    ReturnIndexes = numpy.flatnonzero(pingPwr[StartBin:-1]>NewThreshold)
    
    ReturnIndexes = ReturnIndexes + StartBin
    print pingPwr[ReturnIndexes]

    print 'transbearing in grads',float(msgData[40]+(msgData[41]*256))
    transBearing = ((float(msgData[40]+(msgData[41]*256))/6400.0)*360)  #convert back from 16th of a gradian to degrees (-90 for sonar mounting)
    transBearing = transBearing %360

    if ReturnIndexes != []:
        TargetRange = ReturnIndexes[0] * BinLength
	pub.publish(transBearing=transBearing, rangeToTarget=TargetRange, heading=compass_heading)
    else: 
        TargetRange = -1
        pub.publish(transBearing=transBearing, rangeToTarget=TargetRange, heading=compass_heading)

    print type(transBearing)
    print 'bearing:',transBearing#)/6400)*360
    print 'targetrange:',TargetRange
    print 'range:', Range
    print 'NBins:', NBins
    print 'binLength:', BinLength
    print 'ADInterval:',ADInterval
    print '_____________'
    
    
def compass_callback(compass_data):
    global compass_heading
    compass_heading = compass_data.heading
    
#    BinLength = ((uint8_to_uint16(ADInterval)*0.000000640)*1500)/2
#    StartBin = int(numpy.ceil(BlankDist/BinLength))
    
#    # Which bins are above the detection threshold?
#    detectIdx = numpy.flatnonzero(pingPwr[StartBin:-1]>Threshold)
    
#    detectIdx = numpy.array([1, 2, 3, 4, 5, 10, 12, 15, 17])
    
#    # Case where no glitch detection is in place
#    if ThresholdCount == 0:
#        floorIdx = detectIdx[0]+StartBin-1
#        targetRange = (floorIdx*Range)/NBins
#        print targetRange
#        transBearing = msgData[40]+(msgData[41]*256)
#        print transBearing
#        return
    
    
    #####################BELOW CODE DOES NOT WORK!  GlitchCount must be set to 1
    
#    diffIdx = numpy.diff(detectIdx)
#    print 'DiffIdx:'
#    print diffIdx
    
#    # Setup a vector of zeros
#    tmpVec = numpy.zeros(detectIdx.size-1)
    
#    #Calculate a vector of 0s and 1s from diffIdx where 1=1 and 0 = anything else
#    tmpVec2 = numpy.flatnonzero(diffIdx == 1)
#    tmpVec[tmpVec2] = 1
#    tmpVec3 = numpy.zeros((tmpVec.size+ThresholdCount-1,1))
#    print tmpVec3
#    print numpy.zeros((5-1,1))
#    print tmpVec.conj().transpose()
#    print numpy.zeros((ThresholdCount-idx,1))
        
#    for idx in range(1,ThresholdCount):
#        tmpVec3 = tmpVec3+[numpy.vstack((numpy.zeros((idx-1,1)),tmpVec.conj().T,numpy.zeros((ThresholdCount-idx,1))))]    
        
#    #tmpVec[tmpVec2] = numpy.ones(tmpVec2.size)

#    print tmpVec3
#    print tmpVec
    
#    print diffIdx.size
#    print tmpVec.size    
    

#    #print detectIdx

#    print BlankDist
#    print BinLength


#    print StartBin
#    print Threshold
#    print GlitchCount
#    #transBearing = msgData[27]+(msgData[28]*256)
#    transBearing = msgData[40]+(msgData[41]*256)
    
    #print transBearing

################################################################
def uint8_to_uint16(input8):
    #converts two uint8s to one uint16
    output16 = input8[0]+(input8[1]*256)
    return output16

################################################################
def detectObstacle():
    rospy.init_node('sonar_detectObstacle', anonymous = True)
    rospy.Subscriber('sonar_output', String, callback)
    rospy.spin()

################################################################
if __name__ == '__main__':
    global pub
    global compass_heading
    compass_heading = compass().heading
    pub = rospy.Publisher('sonar_polarRange', sonar_polarRange)
    rospy.Subscriber('compass_out', compass, compass_callback)
    detectObstacle()
      

