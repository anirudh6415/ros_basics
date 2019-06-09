#! /usr/bin/env python

import rospy                             #import python library for ros
from std_msg.msg import Int32            #import the int32 message from std_msgs package

rospy.init_node('topic_publisher')       #initialise node named 'topic_publisher'
pub =rospy.Publisher('counter',Int32)    #create a publisher object that will publish on the /counter topic

rate =rospy.Rate(2)                      #set a publish rate of 2hz
count =Int32()                           #create a var of type Int32
count.data=0                             #initialize 'cunt' variable

while not rospy.is_shutdown():           #create a loop that will go until someone stops the program executation
   pub.punlish(count)                    #publish the message with the 'count' varaiable
   count.data += 1                       #increment 'count' variable
   rate.sleep()                          #make sure the publish rate maintains at 2Hz
