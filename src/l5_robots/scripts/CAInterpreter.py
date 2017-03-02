#!/usr/bin/env python

# Analyse a CA to determine actions, send those actions to the subsumption architecture

import rospy
from l5_robots.msg import CaGrid, CaRow
from std_msgs.msg import Int32
import sys
import numpy as np

# ROI's in format: [(starting x coord, x length), (starting y coord, y length)]
ROIl = rospy.get_param('ROIl')
ROIr = rospy.get_param('ROIr')

# Convert from list of lists to list of tuples
print(ROIl)
print(list(ROIl[0])[0])
ROIl = [(int(x[0]), int(x[1])) for x in ROIl]
ROIr = [(int(x[0]), int(x[1])) for x in ROIr]

THRESH_LIMIT = rospy.get_param('/CAInterpreter/THRESH_LIMIT') # Threshold in percent
REFRESH_LIMIT = rospy.get_param('/CAInterpreter/REFRESH_LIMIT') # Time after which to refresh the oscillator

STRAIGHT = 0
RIGHT = 1
LEFT = 2
BACK = 3

class CAInterpreter():
    def __init__(self):
        rospy.init_node('CAInterpreter', anonymous=False)
        rospy.loginfo("CAInterpreter node started.")
        rospy.on_shutdown(self.shutdown)

        self.refresh_counter = 0
               
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

        try:
            self.refresh_pub = rospy.Publisher("ca/refresh_oscillator", Int32, queue_size=10)
            r = rospy.Rate(10);
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

        tL, rL = self.threshold(ROIl)
        tR, rR = self.threshold(ROIr)


        if (tR and tL):
            if rR > rL:
                self.action_pub.publish(RIGHT)
            elif rR < rL:
                self.action_pub.publish(LEFT)
            else:
                self.action_pub.publish(BACK)
            self.refresh_counter += 2

        elif (tR):
            self.action_pub.publish(RIGHT)
            self.refresh_counter += 2

        elif (tL):
            self.action_pub.publish(LEFT)
            self.refresh_counter += 2

        elif self.refresh_counter > REFRESH_LIMIT:
            self.refresh_pub.publish(BACK)
            self.refresh_pub.publish(BACK)
            self.refresh_pub.publish(BACK)
            self.refresh_counter = 0

        else:
            self.refresh_counter += 10
            self.action_pub.publish(STRAIGHT)

        


    def threshold(self, ROI):
        # Extract ROI in numpy array form
        np_ROI = self.grid[ROI[1][0]:ROI[1][0]+ROI[1][1], ROI[0][0]:ROI[0][0]+ROI[0][1]]

        # Frequency of values in the ROI
        unique, counts = np.unique(np_ROI, return_counts=True)
        occurences = dict(zip(unique, counts))
        print(occurences)

        # How much of the ROI is LIVE
        area = np_ROI.shape[0] * np_ROI.shape[1]
        if 1 in occurences:
            ratio = float(occurences[1]) / float(area)
        else:
            ratio = 0

        print(str(ratio) + " --- " + str(THRESH_LIMIT))

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