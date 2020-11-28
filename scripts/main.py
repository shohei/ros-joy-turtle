#!/usr/bin/python

import rospy
import std_msgs
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

rospy.init_node('server')
rospy.loginfo('server init')

pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

def callback(data):
    msg = Twist()
    msg.linear.x = data.axes[1] 
    msg.angular.z = data.axes[0] 
    rospy.loginfo((data.axes[0],data.axes[1]))
    pub.publish(msg)

sub = rospy.Subscriber('/joy', Joy, callback)

rospy.spin()
