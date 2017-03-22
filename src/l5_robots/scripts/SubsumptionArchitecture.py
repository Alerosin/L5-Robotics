#!/usr/bin/env python

# Basic subsumption architecture
# Trigger some layers based on CA output

import rospy
import random
from geometry_msgs.msg import Twist
from l5_robots.msg import CaGrid
from l5_robots.msg import CaRow
from std_msgs.msg import Int32
from kobuki_msgs.msg import BumperEvent

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
        self.accepting_callbacks = True
        self.flags = [self.right_flag, self.left_flag, self.straight_flag,
                        self.bumperActivated, self.objectTooClose]

        try:
            self.ca = rospy.Subscriber("ca/trigger_layer", Int32, self.callback)
        except Exception as e:
            rospy.loginfo("Error in Subsumption when subscribing to /trigger_layer..")
            print(e)

        try:
            self.bump = rospy.Subscriber("mobile_base/events/bumper", BumperEvent, self.bumperEvent)
        except Exception as e:
            print(e)

        while not rospy.is_shutdown():
            try:
                rospy.spin()
            except Exception as e:
                rospy.loginfo("Error when calling decideLayer..")
                print(e)

    # TODO: CAInterpreter has taken a decision, set the appropriate flag
    def callback(self, data):
        if self.accepting_callbacks == False:
            rospy.loginfo("Discarded callback")
            return

        move_cmd = Twist()

        if data.data == 1:
            #rospy.loginfo("Issuing Right move command")
            move_cmd.linear.x = 0.05
            move_cmd.angular.z = -0.4
            self.cmd_vel.publish(move_cmd)
        elif data.data == 2:
            #rospy.loginfo("Issuing Left move command")
            move_cmd.linear.x = 0.05
            move_cmd.angular.z = 0.4
            self.cmd_vel.publish(move_cmd)
        elif data.data == 3:
            #rospy.loginfo("Issuing Back move command")
            move_cmd.linear.x = -0.2
            move_cmd.angular.z = 0.0
            self.cmd_vel.publish(move_cmd)
        elif data.data == 4:
            rospy.loginfo("Issuing Recover move command")
            self.recover_behaviour()
        else:
            #rospy.loginfo("Issuing Straight move command")
            move_cmd.linear.x = 0.2
            move_cmd.angular.z = 0
            self.cmd_vel.publish(move_cmd)

    def recover_behaviour(self):
        self.accepting_callbacks = False
        move_cmd = Twist()
        turn_angle = 5 * random.sample([1, -1], 1)[0] # Pick 1 int from [1, -1]. Returns a list so need to append [0]

        for i in range(5):
            move_cmd.linear.x = -0.2
            move_cmd.angular.z = 0
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(rospy.Duration(0.03))

        for i in range(10):
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = turn_angle
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(rospy.Duration(0.05))

        self.accepting_callbacks = True

    
    def bumperEvent(self, data):
        rospy.loginfo("Hit a bumper!")
        self.recover_behaviour()



    # Subsumption layer logic - Use the flags to decide what to do
    def decideLayer(self):
        move_cmd = Twist()

        if (self.bumperActivated):
            print("")
        elif (self.objectTooClose):
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
            pass
            #rospy.loginfo("No move command")

        for i in self.flags:
            i = False


    def shutdown(self):
        rospy.loginfo("Stop TurtleBot")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

 
if __name__ == '__main__':
    try:
        SubsumptionArchitecture()
    except:
        rospy.loginfo("SubsumptionArchitecture node terminated.")