#!/usr/bin/env python

# Analyse a CA to determine actions, send those actions to the subsumption architecture

import rospy
from l5_robots.msg import CaGrid, CaRow, InterpreterData
from std_msgs.msg import Int32
import sys
import numpy as np

# ROI's in format: [(starting x coord, x length), (starting y coord, y length)]
ROIl = rospy.get_param('ROIl')
ROIr = rospy.get_param('ROIr')

# Convert from list of lists to list of tuples
ROIl = [(int(x[0]), int(x[1])) for x in ROIl]
ROIr = [(int(x[0]), int(x[1])) for x in ROIr]

THRESH_LIMIT = rospy.get_param('/CAInterpreter/THRESH_LIMIT') # Threshold in percent
REFRESH_LIMIT = rospy.get_param('/CAInterpreter/REFRESH_LIMIT') # Time after which to refresh the oscillator
RECOV_LIMIT = rospy.get_param('/CAInterpreter/RECOV_LIMIT') # Time after which to refresh the oscillator

STRAIGHT = 0
RIGHT = 1
LEFT = 2
BACK = 3
RECOVER = 4

class CAInterpreter():
    def __init__(self):
        rospy.init_node('CAInterpreter', anonymous=False)
        rospy.loginfo("CAInterpreter node started.")
        rospy.on_shutdown(self.shutdown)

        self.refresh_counter = 0
        self.recover_counter = 0
        self.prev_action = 0

        # Create the msg that is used for the info panel in visualiser, add constants.
        self.info_msg = InterpreterData()
        self.info_msg.thresh_limit = THRESH_LIMIT
        self.info_msg.refresh_limit = REFRESH_LIMIT
               
        try:
            rospy.Subscriber("ca/state", CaGrid, self.stateCallback)
        except Exception as e:
            print(e)
            sys.exit(0)

        try:
            self.action_pub = rospy.Publisher("ca/trigger_layer", Int32, queue_size=10)
        except Exception as e:
            print(e)
            sys.exit(0)

        try:
            self.refresh_pub = rospy.Publisher("ca/refresh_oscillator", Int32, queue_size=10)
        except Exception as e:
            print(e)
            sys.exit(0)

        try:
            self.info_pub = rospy.Publisher("ca/interpreter_data", InterpreterData, queue_size=10)
        except Exception as e:
            print(e)
            sys.exit(0)


    # Makes a decision by thresholding ROIs, if nothing is decided, 
    #   increment a counter that will refresh the oscillator after a time
    def stateCallback(self, data):
        self.grid = []
        for row in data.grid:
            self.grid.append([x for x in row.row])
        self.grid = np.asarray(self.grid, dtype=np.uint8)

        action = -1

        tL, rL = self.threshold(ROIl)
        tR, rR = self.threshold(ROIr)

        if (tR and tL):
            if rR > rL:
                action = RIGHT
            elif rR < rL:
                action = LEFT
            else:
                action = BACK
            self.refresh_counter += 2

        elif (tR):
            action = RIGHT
            self.refresh_counter += 2

        elif (tL):
            action = LEFT
            self.refresh_counter += 2

        else:
            self.refresh_counter += 10
            action = STRAIGHT

        if action == self.prev_action:
            self.recover_counter += 1
            if self.recover_counter > RECOV_LIMIT:
                action = RECOVER
        else:
            self.recover_counter = 0


        if self.refresh_counter > REFRESH_LIMIT:
            self.refresh_counter = 0
            self.refresh_pub.publish(0)

        self.info_msg.ROIl_ratio = rL
        self.info_msg.ROIl_thresh = str(tL)
        self.info_msg.ROIr_ratio = rR
        self.info_msg.ROIr_thresh = str(tR)
        self.info_msg.refresh_counter = self.refresh_counter
        # TODO: Find another way of getting the string
        if action == STRAIGHT:
            self.info_msg.action = "Straight"
        elif action == RIGHT:
            self.info_msg.action = "Right"
        elif action == LEFT:
            self.info_msg.action = "Left"
        elif action == BACK:
            self.info_msg.action = "Back"
        elif action == RECOVER:
            self.info_msg.action = "Recover"

        self.prev_action = action
        
        self.info_pub.publish(self.info_msg)
        self.action_pub.publish(action)


    def threshold(self, ROI):
        # Extract ROI in numpy array form
        np_ROI = self.grid[ROI[1][0]:ROI[1][0]+ROI[1][1], ROI[0][0]:ROI[0][0]+ROI[0][1]]

        # Frequency of values in the ROI
        unique, counts = np.unique(np_ROI, return_counts=True)
        occurences = dict(zip(unique, counts))

        # How much of the ROI is LIVE
        area = np_ROI.shape[0] * np_ROI.shape[1]
        if 1 in occurences:
            ratio = float(occurences[1]) / float(area)
        else:
            ratio = 0

        if ratio > THRESH_LIMIT:
            return True, ratio
        else:
            return False, ratio


    def shutdown(self):
        rospy.loginfo("CAInterpreter node shutting down.")


if __name__ == '__main__':
    try:
        CAInterpreter()
        rospy.spin()
    except Exception as e:
        raise e
        print(e)