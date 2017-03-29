#!/usr/bin/env python

# Fake bumper events by checking for distance travelled in a time window.
# If less than a set minimum, issue a bumper event to /mobile_base/event/bumper

import rospy
import random
import LinkedList
import sys
import math
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from std_msgs.msg import Header
from kobuki_msgs.msg import BumperEvent
from nav_msgs.msg import Odometry

MINIMUM_MOVE = 0.002
ACTUAL_MOVE  = 0.0
TIME_WINDOW  = 10        # In seconds
ODOM_FILTER_LIMIT = 500

class FakeBumper():
    # Init ROS node, register for subs/pubs, start loop
    def __init__(self):
        rospy.init_node('FakeBumper', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        

        self.odom_msg_header = Header()
        self.odom_list = LinkedList.LinkedList(TIME_WINDOW)
        self.odom_filter_counter = 0
        self.bumper_msg = BumperEvent()
        self.bumper_msg.bumper = 1
        self.bumper_msg.state = 1
     


        try:
            self.odom_sub = rospy.Subscriber("odom", Odometry, self.odom_callback)
        except Exception as e:
            rospy.loginfo("Couldn't Subscribe to /odom")
            print(e)

        try:
            self.bump_pub = rospy.Publisher("mobile_base/events/bumper", BumperEvent, queue_size=10)
        except Exception as e:
            print(e)

        while not rospy.is_shutdown():
            try:
                rospy.spin()
            except Exception as e:
                rospy.loginfo("Error in FakeBumper")
                print(e)

    def odom_callback(self, data):
        self.odom_filter_counter += 1
        if self.odom_filter_counter < ODOM_FILTER_LIMIT:
            return

        self.odom_filter_counter = 0

        time = data.header.stamp.secs
        point_msg = data.pose.pose.position
        point = [point_msg.x, point_msg.z]

        self.odom_list.add(time, point)
        self.check_distance()


    def check_distance(self):
        (current, first) = self.odom_list.get_points()
        x = math.pow((first[0] - current[0]), 2)
        z = math.pow((first[1] - current[1]), 2)
        dist = math.sqrt(x + z)

        print(dist)
        if dist < MINIMUM_MOVE:
            self.bump_pub.publish(self.bumper_msg)



    def shutdown(self):
        rospy.loginfo("Stop FakeBumper")


 
if __name__ == '__main__':
    try:
        FakeBumper()
    except:
        rospy.loginfo("FakeBumper node terminated.")