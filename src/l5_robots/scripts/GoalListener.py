#!/usr/bin/env python3

# Analyse a CA to determine actions, send those actions to the subsumption architecture

import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Pose, Point
from std_msgs.msg import Int32
import sys
import numpy as np

TIME_LIMIT = (20 * 60) - 1 # Time limit in minutes * seconds

# Class that checks to see if the robot has reached the goal.
# It also times the robot, and shutsdown all nodes upon completion.
class CAInterpreter():
    def __init__(self):
        rospy.init_node('GoalListener', anonymous=False)
        rospy.loginfo("GoalListener node started.")
        rospy.on_shutdown(self.shutdown)

        self.start = rospy.Time.now()

               
        try:
            rospy.Subscriber("/gazebo/model_states", ModelStates, self.stateCallback)
        except Exception as e:
            print(e)
            sys.exit(0)

        try:
            self.goalPub = rospy.Publisher("ca/goal_reached", Int32, queue_size=10)
        except Exception as e:
            print(e)
            sys.exit(0)



    # Makes a decision by thresholding ROIs, if nothing is decided, 
    #   increment a counter that will refresh the oscillator after a time
    def stateCallback(self, data):
        pose = data.pose[-1]
        point = pose.position
        
        if (point.y < 0):
            rospy.loginfo(pose)
            self.goalPub.publish(1)

            self.end = rospy.Time.now()
            rospy.loginfo("REACHED GOAL")
            rospy.loginfo("START TIME: " + str(self.start.secs))
            rospy.loginfo("END TIME: " + str(self.end.secs))
            rospy.signal_shutdown("Goal Reached")
        elif (rospy.Time.now().secs > TIME_LIMIT):
            rospy.loginfo(pose)
            self.goalPub.publish(0)

            self.end = rospy.Time.now()
            rospy.loginfo("TIME IS UP")
            rospy.loginfo("START TIME: " + str(self.start.secs))
            rospy.loginfo("END TIME: " + str(self.end.secs))
            rospy.signal_shutdown("Exceeded Time Limit")






    def shutdown(self):
        rospy.loginfo("GoalListener node shutting down.")


if __name__ == '__main__':
    try:
        CAInterpreter()
        rospy.spin()
    except Exception as e:
        raise e
        print(e)