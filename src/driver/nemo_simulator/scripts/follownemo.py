#!/usr/bin/env python3
import rospy
import geometry_msgs.msg as gm
import std_msgs.msg
import numpy 

def callback(msg):
    msg.x

if __name__ == '__main__':
    rospy.Subscriber("/sonar_data", gm.PointStamped, callback)
    