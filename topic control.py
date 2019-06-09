create a file in src of your pacakge like control.py

#! /usr/bin/env python

import rospy                                           #import python library for ros
from std_msgs.msg import Int32                         #import the int32 message from std_msgs package

rospy.init_node('topic_publisher')                     #initiate node named 'topic_publisher'
pub =rospy.Publisher('/control',Int32,queue_size=1)    #create a publisher object that will publish on the /counter topic
                                                       #messages of type Int32
rate =rospy.Rate(2)                                    #set a publish rate of 2hz
count =Int32()                                         #create a var of type Int32
count.data=0                                           #initialize 'cunt' variable

while not rospy.is_shutdown():                         #create a loop that will go until someone stops the program executation
   pub.publish(count)                                  #publish the message with the 'count' varaiable
   count.data += 1                                     #increment 'count' variable
   rate.sleep()                                        #make sure the publish rate maintains at 2Hz

   
   
>now run the above code by :
   rosrun <pacakage_name> <file_name>
   
 in my case it was :
ros@ros:~/catkin_ws$ rosrun beginner_tutorials control.py 

nothing would appear 

>so press ctr+shift+t in terminal sub-terminal would appear then :
   rostopic lsit | grep /control
   /control (would appear)
   
then:
ros@ros:~/catkin_ws$ rostopic info /control 
Type: std_msgs/Int32

Publishers: 
 * /topic_publisher (http://ros:43203/)

Subscribers: None
   
the above would appear 

ros@ros:~/catkin_ws$ rostopic echo /control
data: 1045
---
data: 1046
---
data: 1047
---
data: 1048
---
data: 1049
---
data: 1050
---
data: 1051
---
....... continues 
press ctr+c to stop 


"""so basically what code does is creating a publisher and publishing a messesge of type Int32 on /control topic""" 

then question arises what is Publisher ??
Publisher is a node that keeps publishing into  a topic .
then what is topic topic is a channel that acts as a pipe where other ROS node can either 
publish or read infromation.



