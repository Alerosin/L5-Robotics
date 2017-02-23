#!/usr/bin/env python

# Listens to /ca/state, visualises the grid

import rospy
from l5_robots.msg import CaGrid, CaRow
import matplotlib.pyplot as plt
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError
import sys

class CAVisualiser():
    def __init__(self):
        rospy.init_node('CAVisualiser', anonymous=False)
        rospy.loginfo("CAVisualiser node started.")
        rospy.on_shutdown(self.shutdown)

        self.window = "CA Visualiser"
        self.image_scale = 20
               
        try:
            rospy.Subscriber("ca/state", CaGrid, self.stateCallback)
        except Exception as e:
            print(e)
            sys.exit(0)


    def shutdown(self):
        rospy.loginfo("CAVisualiser node shutting down.")
        cv2.destroyAllWindows()


    def stateCallback(self, data):
        rospy.loginfo("Start cb.")
        self.grid = []
        for r in data.grid:
            row = []
            for x in r.row:
                row.append(int(x))
            self.grid.append(row)

        self.grid = np.asarray(self.grid, dtype='uint8')
        self.grid *= 120

        
        res = cv2.resize(self.grid, None, fx=self.image_scale, fy=self.image_scale, 
                            interpolation = cv2.INTER_AREA)

        #self.grid *= 0

        #cv2.imshow(self.window, self.grid) # Set Image to black
        cv2.imshow(self.window, res)
        cv2.waitKey(10)



if __name__ == '__main__':
    try:
        CAVisualiser()
        rospy.spin()
    except Exception as e:
        raise e