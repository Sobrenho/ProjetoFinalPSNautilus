#!/usr/bin/env python3
import rospy
import geometry_msgs.msg as gm
import math

class follownemo:
    def __init__(self):
        self.pub = rospy.Publisher("/cmd_vel", gm.Twist, queue_size=10)

    def getVel(self, msg):
        vel = gm.Twist()

        normal = math.sqrt(msg.point.x**2 +  msg.point.y**2 + msg.point.z**2)

          
        vel.linear.x = -2 * msg.point.x/normal
        vel.linear.y = -2 * msg.point.y/normal
        vel.linear.z = -2 * msg.point.z/normal

        if abs(msg.point.x) < 2.5:
            vel.linear.x = 0
        if abs(msg.point.y) < 2.5:
            vel.linear.y = 0
        if abs(msg.point.z) < 2.5:
            vel.linear.z = 0

                
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0

        self.pub.publish(vel)

    def start(self):
        rate = rospy.Rate(rospy.get_param("rate"))
        while not rospy.is_shutdown():
            rospy.Subscriber("/sonar_data", gm.PointStamped, self.getVel)
            rate.sleep()
            rospy.spin()


if __name__ == '__main__':
    rospy.init_node("follownemo", anonymous=True)
    try:
        f = follownemo()
        f.start()
        
    except rospy.ROSInterruptException:
        pass

    
        

        