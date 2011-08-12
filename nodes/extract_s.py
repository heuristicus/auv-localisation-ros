#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
import sys
import serial
import time
import numpy
from std_msgs.msg import String
from loc_sonar.msg import sonar_return

################################################################
def callback(msgData):    
    data = sonar_return()
    #read the msgData into a numpy array for processing
    msgData = numpy.fromstring(msgData.data, dtype=numpy.uint8)
    #Byte 14,15:
    totalLength = uint8_to_uint16([msgData[13], msgData[14]])
    data.length = int(totalLength)
    # print 'total length of message:', totalLength
 
    #Byte 17:
    headstatus = msgData[16]
    hdstat = headstatus
    #print 'head status', headstatus

    #Byte 19,20:
    hdctrl1 = msgData[18]
    hd1 = hdctrl1
    #print 'HdCtrl bits (byte 1) - convert to binary and see manual for description:', hdctrl1
    hdctrl2 = msgData[19]
    hd2 = hdctrl2
    #print 'HdCtrl bits (byte 2) - convert to binary and see manual for description:', hdctrl2
   

    #Byte 21,22:
    rangescale = uint8_to_uint16([msgData[20], msgData[21]])
    rng = rangescale
    #print 'range scale:', rangescale 

    #Byte 34,35:
    ADInterval = uint8_to_uint16([msgData[33], msgData[34]])
    ad = ADInterval
    #print 'ADInterval:', ADInterval 

    #Byte 36,37:
    LeftLimit = uint8_to_uint16([msgData[35], msgData[36]])
    llim = LeftLimit
    #print 'left limit of sonar sweep (1/16th gradian):', LeftLimit

    #Byte 38,39:
    RightLimit = uint8_to_uint16([msgData[37], msgData[38]])
    rlim = RightLimit
    #print 'right limit of sonar sweep (1/16th gradian):', RightLimit

    #Byte 40:
    StepAngleSize = msgData[39]
    step = StepAngleSize
    #print 'step size (between each ping) (1/16th gradian):', StepAngleSize

    #Bytes 41,42:
    transBearing = uint8_to_uint16([msgData[40], msgData[41]])
    bear = transBearing
    #print 'bearing of transducer (1/16th gradian):', transBearing
    transBearingDeg = ((float(msgData[40]+(msgData[41]*256))/6400.0)*360)  #convert back from 16th of a gradian to degrees
    transBearingDeg = transBearingDeg %360
    beardeg = transBearingDeg
    #print 'bearing of transducer (degrees):', transBearingDeg

    #Byte 43,44:
    nBins = uint8_to_uint16([msgData[42], msgData[43]])
    nbins = nBins
    #print 'number of bins:', nBins

    #data bytes:
    #print 'bin data:', msgData[44:-1] 
    bins = msgData[44:-1]
    #print bins
    #params = {'length':length, 'hdstat':hdstat, 'hd1':hd1, 'hd2':hd2, 'rng':rng, 'ad':ad, 'llim':llim, 'rlim':rlim, 'step':step, 'bear':bear, 'beardeg':beardeg, 'nbins':nbins}
    pub.publish(data)
    #print '_____________'

    
    
################################################################
def uint8_to_uint16(input8):
    #converts two uint8s to one uint16
    output16 = input8[0]+(input8[1]*256)
    return output16

################################################################
def detectObstacle():
    global pub
    rospy.init_node('sonar_extractParameters', anonymous = True)
    rospy.Subscriber('sonar_output', String, callback)
    pub = rospy.Publisher('sonar_info', sonar_return)
    rospy.spin()

################################################################
if __name__ == '__main__':
    detectObstacle()


