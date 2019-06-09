""" it is a simple python file created in src folder in your pakage """"

#! /usr/bin/env python #always use whenever you create a python file

import rospy 

rospy.init_node('ObiWan') #inisiating node ObiWan
rate=rospy.Rate(2)        #rate of 2Hzs
while not rospy.is_shutdown(): #endless loop until shutdown means ctr+c
	print(" help me")       
	rate.sleep()  
  
  
