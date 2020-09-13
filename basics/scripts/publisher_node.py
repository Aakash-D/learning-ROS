#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node('publisher_node', anonymous=False)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        msg = "Hello ROS %s" % rospy.get_time()
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
