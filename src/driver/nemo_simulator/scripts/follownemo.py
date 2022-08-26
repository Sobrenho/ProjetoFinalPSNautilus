#!/usr/bin/env python3
import rospy
import geometry_msgs.msg as gm


def callback(msg: gm.PointStamped):
    pub = rospy.Publisher("/cmd_vel", gm.Twist, queue_size=10)

    vel = gm.Twist()
    

    vel.linear.x = -msg.point.x
    vel.linear.y = -msg.point.y
    vel.linear.z = -msg.point.z

    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0
   
    pub.publish(vel)


    

if __name__ == '__main__':
    rospy.init_node("follownemo", anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()       
        rospy.Subscriber("/sonar_data", gm.PointStamped, callback)
        

        