#!/usr/bin/env python3
import rospy
import geometry_msgs.msg as gm

class follownemo:
    def __init__(self):
        rospy.init_node("follownemo", anonymous=True)
        self.pub = rospy.Publisher("/cmd_vel", gm.Twist, queue_size=10)

    def getVel(self, msg: gm.PointStamped):
        vel = gm.Twist()

        noise = rospy.get_param("/noise-mag")

        vel.linear.x, vel.linear.y, vel.linear.z = 0,0,0
        

        if abs(msg.point.x) > 2.2:
            vel.linear.x = -(msg.point.x - noise)/3.5
        
        if abs(msg.point.y)  > 2.2:
            vel.linear.y = -(msg.point.y - noise)/3.5

        if msg.point.z > 0.3:  
            vel.linear.z = -(msg.point.z- noise)/3.5 - 0.2

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

    
        

        