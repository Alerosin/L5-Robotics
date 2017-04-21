#!/usr/bin/env python3

# Basic subsumption architecture
# Trigger some layers based on CA output

import rospy
import random
from geometry_msgs.msg import Twist
from l5_robots.msg import CaGrid
from l5_robots.msg import CaRow
from std_msgs.msg import Int32
from kobuki_msgs.msg import BumperEvent

TYPE = rospy.get_param('/SubsumptionArchitecture/TYPE')
if TYPE == "base":
    CA_ACTIVE = False
else:
    CA_ACTIVE = True

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
        self.bumperActivated = [False, False, False] # Left, Centre and right bumper
        self.objectTooClose = False
        self.accepting_callbacks = True
        self.flags = [self.right_flag, self.left_flag, self.straight_flag,
                        self.bumperActivated, self.objectTooClose]
        self.interp_result = 0

        try:
            self.ca = rospy.Subscriber("ca/trigger_layer", Int32, self.callback)
        except Exception as e:
            rospy.loginfo("Error in Subsumption when subscribing to /trigger_layer..")
            print(e)

        try:
            self.bump = rospy.Subscriber("mobile_base/events/bumper", BumperEvent, self.bumperEvent)
        except Exception as e:
            print(e)

        if (CA_ACTIVE):
            while not rospy.is_shutdown():
                self.act()
        else:
            while not rospy.is_shutdown():
                self.base_act()


    def act(self):
        if self.accepting_callbacks == False:
            return

        self.accepting_callbacks = False

        if (self.bumperActivated[1] == True):   # Front bumper
            rospy.loginfo("FRONT")
            self.go_back()
            self.do_180()
            self.bumperActivated[1] = False
        elif (self.bumperActivated[0] == True): # Left bumper
            self.go_back()
            self.turn_right()
            self.bumperActivated[0] = False
        elif (self.bumperActivated[2] == True): # Right bumper
            self.go_back()
            self.turn_left()
            self.bumperActivated[2] = False
        elif (self.interp_result == 1):         # ROI trigger Right 
            self.go_right()
        elif (self.interp_result == 2):         # ROI trigger Left
            self.go_left()
        elif (self.interp_result == 0):         # Straight
            self.straight()

        self.accepting_callbacks = True

    def base_act(self):
        if self.accepting_callbacks == False:
            return

        rospy.loginfo("using base")
        self.accepting_callbacks = False

        if (self.bumperActivated[1] == True):   # Front bumper
            rospy.loginfo("FRONT")
            self.go_back()
            self.do_180()
            self.bumperActivated[1] = False
        elif (self.bumperActivated[0] == True): # Left bumper
            self.go_back()
            self.turn_right()
            self.bumperActivated[0] = False
        elif (self.bumperActivated[2] == True): # Right bumper
            self.go_back()
            self.turn_left()
            self.bumperActivated[2] = False
        else:         # Straight
            self.straight()

        self.accepting_callbacks = True


    # TODO: CAInterpreter has taken a decision, set the appropriate flag
    def callback(self, data):
        self.interp_result = data.data


    def go_back(self):
        move_cmd = Twist()
        move_cmd.linear.x = -0.4
        move_cmd.angular.z = 0
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(rospy.Duration(0.2))
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(rospy.Duration(0.1))
        rospy.loginfo("go_back")

    def turn_left(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 1.5
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(rospy.Duration(0.3))
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(rospy.Duration(0.3))
        self.cmd_vel.publish(move_cmd)
        #rospy.loginfo("turn_left")

    def turn_right(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = -1.5
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(rospy.Duration(0.3))
        self.cmd_vel.publish(move_cmd)
        rospy.sleep(rospy.Duration(0.3))
        self.cmd_vel.publish(move_cmd)
        #rospy.loginfo("turn_right")

    def go_left(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.1
        move_cmd.angular.z = 0.5
        self.cmd_vel.publish(move_cmd)
        #rospy.loginfo("go_left")

    def go_right(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.1
        move_cmd.angular.z = -0.5
        self.cmd_vel.publish(move_cmd)
        #rospy.loginfo("go_right")

    def do_180(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 1.4
        for i in range(8):
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(rospy.Duration(0.3))
        #rospy.loginfo("180")

    def straight(self):
        move_cmd = Twist()
        move_cmd.linear.x = 0.4
        move_cmd.angular.z = 0.0
        self.cmd_vel.publish(move_cmd)
        #rospy.loginfo("straight")


    
    def bumperEvent(self, data):
        if (data.state == 0): # If the bumper was just released, return
            return

        b = data.bumper

        # Left, Centre and Right bumpers
        if (b == 0):
            self.bumperActivated[0] = True
        elif (b == 1):
            self.bumperActivated[1] = True
        elif (b == 2):
            self.bumperActivated[2] = True



    def shutdown(self):
        rospy.loginfo("Stop TurtleBot")

 
if __name__ == '__main__':
    try:
        SubsumptionArchitecture()
    except:
        rospy.loginfo("SubsumptionArchitecture node terminated.")
