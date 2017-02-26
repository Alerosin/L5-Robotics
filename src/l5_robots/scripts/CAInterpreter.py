#!/usr/bin/env python

# Analyse a CA to determine actions, send those actions to the subsumption architecture

import rospy
from l5_robots.msg import CaGrid, CaRow
from std_msgs.msg import Int32
import sys

class CAInterpreter():
    def __init__(self):
        rospy.init_node('CAInterpreter', anonymous=False)
        rospy.loginfo("CAInterpreter node started.")
        rospy.on_shutdown(self.shutdown)
               
        try:
            rospy.Subscriber("ca/state", CaGrid, self.stateCallback)
        except Exception as e:
            print(e)
            sys.exit(0)

        try:
            self.action_pub = rospy.Publisher("ca/trigger_layer", Int32, queue_size=10)
            r = rospy.Rate(10);
        except Exception as e:
            print(e)
            sys.exit(0)

        while not rospy.is_shutdown():
            r.sleep()

    def stateCallback(self, data):
        # TODO: Analyse CA, publish some integer representing an action to ca/action
        print("TODO: Interpreter")

    def shutdown(self):
        rospy.loginfo("CAInterpreter node shutting down.")
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        CAInterpreter()
    except Exception as e:
        raise e
        print(e)