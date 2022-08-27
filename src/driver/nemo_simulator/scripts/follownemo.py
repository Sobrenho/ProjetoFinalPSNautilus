#!/usr/bin/env python3
import rospy
import geometry_msgs.msg as gm

class follownemo:
    def __init__(self):
        rospy.init_node("follownemo", anonymous=True)
        self.pub = rospy.Publisher("/cmd_vel", gm.Twist, queue_size=10)

    def getVel(self, msg: gm.PointStamped):
        vel = gm.Twist()

        vel.linear.x = -msg.point.x
        vel.linear.y = -msg.point.y
        vel.linear.z = -msg.point.z

        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
    
        self.pub.publish(vel)

    def start(self):
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            rate.sleep()       
            rospy.Subscriber("/sonar_data", gm.PointStamped, self.getVel)

    

if __name__ == '__main__':
    try:
        f = follownemo()
        f.start()
    except rospy.ROSInterruptException:
        pass

    
        

        