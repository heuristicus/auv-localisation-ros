#!/usr/bin/python
import roslib; roslib.load_manifest('loc_sonar')
import rospy
import sys
import serial
import time
import numpy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from loc_sonar.msg import sonar
#from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg

### to do:
### make another version for N/E position estimate that takes in compass heading
### set flags for various modes (wall following, position, scan all)

################################################################
def sonarTalker():
    # defines and sends the ping trigger (mtSendData) to the sonar. 
    global serialPort 
    #trigger = [64, 48, 48, 48, 67, 12, 0, 255, 2, 7, 25, 128, 255, 0, 0, 0, 0, 10]
    
    # construct message using parameters/constants
    AsciiBlock = [64, 48, 48, 48, 67] # @000C - ASCII header to msg
    hexLength = [12, 0] # Length of block in 2 bit int
    SID = rospy.get_param("/SID")
    DID = rospy.get_param("/DID")
    count = 7 # Number of bytes following count byte - excluding LF character 
    msgNum = 25 # Msg identification number
    msgSeq = rospy.get_param("/msgSeq")
    Node = rospy.get_param("/Node")
    currentTime = [0,0,0,0] # current time for sonar, not required for imaging as signals not time stamped
    LF = 10

    mtSendData = AsciiBlock + hexLength + [SID, DID, count, msgNum, msgSeq, Node] + currentTime + [LF]
    mtSendData = ''.join([chr(char) for char in mtSendData[:]])
    serialPort.write(mtSendData)
    # print:
    print "Sending ping trigger to sonar - mtSendData:"
    print mtSendData
    print "--------"


################################################################
def sonarListener():
    # reads in the ping reply from the sonar (mtHeadData), determines the message type and publishes the ping data if applicable
    global serialPort
    print "No. of chars in buffer:"
    print serialPort.inWaiting()
    if serialPort.inWaiting() > 12:
	# read message header, first 13 bytes (as specified in SonarPing.m)
        headerData = serialPort.read(13)
        #print headerData
	headerData = numpy.fromstring(headerData, dtype=numpy.uint8)       
	# print:
	print "Data from sonar: mtHeadData:"
        print headerData
        print "--------"

	if headerData[0] == 64:
	    msgType = headerData[10]
            print "Message type:"
	    print msgType
	   
	    # From sonarPing.m: get the length of the rest of the data
            #    calulate from mtAlive 22 bytes in total, header[5:7] = 16 bytes and we load in 13 bytes initially
	    #    thus number to remove = 16 - (22-13) = 7
	    # headerData[5]+headerData[6]*256 = simulating Matlab typecast function - converting 2 uint8s to 1 uint16  
	    msgLength = (headerData[5]+(headerData[6]*256))-7
	    print msgLength
	    print serialPort.inWaiting()

	    timeOut = 0.1/(24*3600)
	    startTime = time.time()

	    # makes sure full message has been read - may not be needed, but present in sonarPing.m
	    while serialPort.inWaiting()<msgLength:
		print 'looping'
		if startTime+timeOut < time.time():
		    print "Timeout error"
		    return

 	    msgData = serialPort.read(serialPort.inWaiting()) # read rest of message
	    msgData = numpy.fromstring(msgData, dtype=numpy.uint8)   
            print msgData
   	   
	    # if msgData does not end in LF character - could I do this without converting to a numpy array?
	    if msgData[-1] != 10:
	 	print "Message error: missing LF character" 
                serialPort.flushInput()
                return

	    if msgType == 1:
		print "mtVersionData"
		# mtVersionData
	    elif msgType == 2:
		print "mtHeadData"
		#pingPwr = msgData[31:-1]
		#print pingPwr
		transBearing = msgData[27]+(msgData[28]*256)
                
                #TEST LINE:
                msgData = numpy.concatenate((headerData,msgData))
                
		#print msgData[28]
		print transBearing
		print "Publishing...."
	
       		pub = rospy.Publisher('sonar_output', String)
 		msgData = ''.join([chr(char) for char in msgData[:]])
		pub.publish(str(msgData))

            elif msgType == 4:
		print "mtAlive"
		return 4
            else:
		print "Error: Unknown message type"
		
	        
        else:
 	    print "Message error: @" 
            serialPort.flushInput()
            return
            
    
################################################################    
def setupSonar():
    # sends the setup command (mtHeadCommand) to the sonar - NEEDS EDITING TO ADD CALLBACK FUNCTION AND UPDATE FROM PARAMETER DATABASE
    rospy.init_node('sonar')
    global serialPort 
    # settings for Micron Sonar
    serialPort = serial.Serial(port='/dev/ttyUSB0', baudrate='57600 ')
    serialPort.bytesize = serial.EIGHTBITS
    serialPort.stopbits = serial.STOPBITS_ONE
    serialPort.parity = serial.PARITY_NONE
    print "Setup sonar: mtHeadCommand:"
    print serialPort.portstr
    print serialPort.isOpen()

    #setupData = [64, 48, 48, 51, 67, 60, 0, 255, 2, 55, 19, 128, 255, 1, 1, 35, 11, 102, 102, 102, 5, 102, 102, 102, 5, 112, 61, 10, 9, 112, 61, 10, 9, 40, 0, 60, 0, 128, 12, 128, 12, 210, 0, 84, 84, 125, 0, 125, 0, 25, 64, 208, 0, 144, 1, 244, 1, 100, 0, 64, 6, 1, 0, 0, 0, 10]
    flag = 0
    while(flag !=4):
    	setupData = get_mtHeadCommand()
    	serialPort.write(setupData)
        time.sleep(0.1)
	
        print 'still waiting for mtAlive....'
    	flag = sonarListener()

    setupData = get_mtHeadCommand()
    print setupData
    print "--------"
    serialPort.write(setupData)


################################################################
def get_mtHeadCommand():
    # hard-coded as specific to this message:
    AsciiBlock= [64, 48, 48, 51, 67] # @003C - ASCII header to msg 
    hexLength = [60, 0] # Length of block in 2 bit int
    count = 55 		# Number of bytes following count byte - excluding LF character
    msgNum = 19 	# Msg identification number
    
    # construct message using parameters
    SID = rospy.get_param("/SID")
    DID = rospy.get_param("/DID")

    headType = rospy.get_param("/headType")

    msgSeq = rospy.get_param("/msgSeq")
    Node = rospy.get_param("/Node")
  
    HdCtrl1 = int(rospy.get_param("/HdCtrl1"),2)
    HdCtrl2 = int(rospy.get_param("/HdCtrl2"),2)

    DstHead = rospy.get_param("/DstHead")
    TXNChan = [102, 102, 102, 5] # Hard coded as not used by DST sonars
    RXNChan = [112, 61, 10, 9] # Hard coded as not used by DST sonars

    txPulseLength = [40, 0] # Hard coded as not used by DST sonars
    rangeScale = [60, 0] # Hard coded as not used by sonar head

    # CURRENTLY DESIGNED TO POINT AND PING (LIKE SONARPING.M)
    #LLim = uint16_to_uint8(rospy.get_param("/LLim"))  # anti-clockwise scan limit in 1/16th of a gradian
    #RLim = uint16_to_uint8(rospy.get_param("/RLim"))  # clockwise scan limit in 1/16th of a gradian
   
    LLim = rospy.get_param("/LLim")  # convert anti-clockwise scan limit from degrees to 16ths of a gradian (+90 accounts for sonar mounting)
    LLim = (LLim   )%360
    LLim = LLim/360.0 * 6400
    print LLim
    RLim = rospy.get_param("/RLim")   # clockwise scan limit from degrees to 16ths of a gradian (+90 accounts for sonar mounting)
    RLim = (RLim   )%360
    RLim = RLim/360.0 * 6400
    print RLim

    LLim = uint16_to_uint8(int(LLim))
    RLim = uint16_to_uint8(int(RLim))

    print LLim 
    print RLim

    ADSpan = rospy.get_param("/ADSpan")
    ADLow = rospy.get_param("/ADLow")

    IGainB1 = rospy.get_param("/IGainB1")
    IGainB2 = rospy.get_param("/IGainB2")

    Slope = [125, 0, 125, 0] # Hard coded as not used by DST sonars

    moTime = rospy.get_param("/moTime")
    step = rospy.get_param("/step")
    print step
    
    NBins = rospy.get_param("/NBins")
    Range = rospy.get_param("/Range")
   
    ADInterval = uint16_to_uint8(int(round((((Range*2)/1500.0)/NBins)/0.000000640,0))) 
    rospy.set_param("/ADInterval", ADInterval) #updates ADInterval to parameter server for user in sonar_detect_obstacle

    NBins = uint16_to_uint8(NBins)
    
    MaxADBuf = uint16_to_uint8(rospy.get_param("/MaxADBuf"))
    Lockout = uint16_to_uint8(rospy.get_param("/Lockout"))
    MinorAxis = uint16_to_uint8(rospy.get_param("/MinorAxis"))
    MajorAxis = rospy.get_param("/MajorAxis")

    Ctl2 = rospy.get_param("/Ctl2")
    ScanZ = [0, 0] # Hard coded as always set to 0
    LF = 10 # Hard coded as always set to 10

    # constructs mtHeadCommand to send to sonar
    mtHeadCommand = AsciiBlock + hexLength + [SID, DID, count, msgNum, msgSeq, Node, headType, HdCtrl1, HdCtrl2, DstHead] + TXNChan + TXNChan + RXNChan + RXNChan + txPulseLength + rangeScale + LLim + RLim +[ADSpan, ADLow, IGainB1, IGainB2] + Slope + [moTime, step] + ADInterval+ NBins + MaxADBuf + Lockout + MinorAxis + [MajorAxis, Ctl2] + ScanZ + [LF]

    mtHeadCommand = ''.join([chr(char) for char in mtHeadCommand[:]])
    return mtHeadCommand

################################################################
def uint16_to_uint8(input16):
    #converts a single uint16 to two uint8s
    B1 = int(numpy.uint8(input16))
    B2 = (input16-B1)/256
    output8 = [B1, B2]
    return output8

################################################################
def callback(data):
    print "UPDATE CALLBACK TRIGGERED!!!"
    global updateFlag
    updateFlag = 1
    #rospy.set_param("/heading", int(data.data))
    rospy.set_param("/LLim", int(data.LLim))
    rospy.set_param("/RLim", int(data.RLim))

################################################################
def sonarLoop():
    # controls sonar message sequence (mtSendData->, ->mtHeadData, mtSendData->, ->mtHeadData,... etc. 

    #rospy.init_node('sonar')
    #rospy.Subscriber('sonar_update', String, callback)
    rospy.Subscriber('sonar_update', sonar, callback)
    global updateFlag
    global serialPort
    updateFlag = 0

    setupSonar()
    serialPort.flushInput()

    while not rospy.is_shutdown():
        sonarTalker()
	# 1 second recommended in manual (FAQ) - 0.1 seems to work ok on my laptop - NEED TO CHECK PING RETURNS TO MAKE SURE THIS IS THE CASE       
	time.sleep(0.1)
        print updateFlag
        sonarListener()
        if updateFlag == 1:
            print 'HELLO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
            setupData = get_mtHeadCommand()
	    serialPort.write(setupData)
 	    updateFlag = 0;

def shutdown():
    global serialPort
    serialPort.flushInput()
    serialPort.flushOutput()


################################################################
################################################################
if __name__ == '__main__':
    #needs updating once message structure is sorted...
    rospy.init_node('sonar')
    #rospy.Subscriber('sonar_update', String, callback)
    global updateFlag
    updateFlag = 0
    rospy.on_shutdown(shutdown)

    #setupSonar()
    #serialPort.flushInput()
    sonarLoop()    
    
