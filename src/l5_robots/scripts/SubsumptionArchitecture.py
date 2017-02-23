#!/usr/bin/env python

# Basic subsumption architecture
# Trigger some layers based on CA output

import rospy
from geometry_msgs.msg import Twist
from l5_robots.msg import CaGrid
from l5_robots.msg import CaRow

class SubsumptionArchitecture():
    # Init ROS node, register for subs/pubs, start loop
    def __init__(self):
        rospy.init_node('SubsumptionArchitecture', anonymous=False)
        rospy.on_shutdown(self.shutdown)

        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        r = rospy.Rate(10);

        self.right_flag = False
        self.left_flag = False
        self.straight_flag = False
        self.bumperActivated = False
        self.objectTooClose = False
        self.flags = [self.right_flag, self.left_flag, self.straight_flag,
                        self.bumperActivated, self.objectTooClose]

        try:
            self.ca = rospy.Subscriber("ca/trigger_layer", Int32, callback)
        except Exception as e:
            print("Alright then")
            self.ca = []

        while not rospy.is_shutdown():
            try:
                self.decideLayer()
            except Exception as e:
                rospy.loginfo("Error when calling decideLayer..")
                print(e)
            r.sleep()

    # TODO: CAInterpreter has taken a decision, set the appropriate flag
    def callback(data):
        # Reset Flags
        for i in self.flags:
            e = False

        if data == 1:
            right_flag = True
        elif data = 2:
            left_flag = True
        else:
            straight_flag = True


    # Subsumption layer logic - Use the flags to decide what to do
    def decideLayer(self):
        move_cmd = Twist()

        if (bumperActivated):
            print("")
        elif (objectTooClose):
            print("")
        elif (self.right_flag):
            rospy.loginfo("Issuing Right move command")
            move_cmd.linear.x = 0.1
            move_cmd.angular.z = 0.2
            self.cmd_vel.publish(move_cmd)
        elif (self.left_flag):
            rospy.loginfo("Issuing Left move command")
            move_cmd.linear.x = 0.1
            move_cmd.angular.z = -0.2
            self.cmd_vel.publish(move_cmd)
        elif (self.straight_flag):
            rospy.loginfo("Issuing Straight move command")
            move_cmd.linear.x = 0.1
            move_cmd.angular.z = 0
            self.cmd_vel.publish(move_cmd)
        else:
            rospy.loginfo("No move command")


    def shutdown(self):
        rospy.loginfo("Stop TurtleBot")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

 
if __name__ == '__main__':
    try:
        SubsumptionArchitecture()
    except:
        rospy.loginfo("SubsumptionArchitecture node terminated.")