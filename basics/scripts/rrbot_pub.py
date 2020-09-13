#! /usr/bin/env python

import rospy
from std_msgs.msg import Float64
import math

def commander():
    rospy.init_node('rrbot_pub', anonymous=False)
    pub_jnt1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size=10)
    pub_jnt2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size=10)
    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        pos_jnt1 = math.pi/2
        pos_jnt2 = math.pi/2

        rospy.loginfo("joint 1 position is:  %f" % pos_jnt1)
        pub_jnt1.publish(pos_jnt1)

        rospy.loginfo("joint 2 position is:  %f" % pos_jnt2)
        pub_jnt2.publish(pos_jnt2)

        rate.sleep()

if __name__ == '__main__':
    try:
        commander()
    except rospy.ROSInterruptException:
        pass
