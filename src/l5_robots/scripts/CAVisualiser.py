#!/usr/bin/env python

# Listens to /ca/state, visualises the grid

import rospy
from l5_robots.msg import CaGrid, CaRow
import matplotlib.pyplot as plt
import numpy as np
import math
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import sys

# Colour mappings in BGR
COLOURS = {
    0: (0, 0, 0), # Background is dark grey
    1: (255, 255, 255),       # CA is white
    2: (0, 150, 255)    # Obstacles are orange
}

class CAVisualiser():
    def __init__(self):
        rospy.init_node('CAVisualiser', anonymous=False)
        rospy.loginfo("CAVisualiser node started.")
        rospy.on_shutdown(self.shutdown)

        # Variables controlling custom visualiser window (OpenCV)
        self.window = "CA Visualiser"
        self.image_scale = 15

        # Construct nunpy arrays used to convert 2D grayscale to 3D BGR
        self.b_map = np.array([COLOURS[mapping][0] for mapping in COLOURS])
        self.g_map = np.array([COLOURS[mapping][1] for mapping in COLOURS])
        self.r_map = np.array([COLOURS[mapping][2] for mapping in COLOURS])

        # Included in Header of Image msg
        self.image_id = 0
               
        try:
            rospy.Subscriber("ca/state", CaGrid, self.stateCallback)
        except Exception as e:
            print(e)
            sys.exit(0)


    def shutdown(self):
        rospy.loginfo("CAVisualiser node shutting down.")
        cv2.destroyAllWindows()

    def drawScanLines(self):
        line_colour = (255, 0, 0)
        line_px_width = 1 
        height, width = self.res.shape
        P1 = (int(width/2), height/2)

        P2 =  (int(P1[0] + (width/2) * math.cos(-0.200776875019)), 
                int(P1[1] + (width/2) * math.sin(0.200776875019)))

        P3 =  (int(P1[0] + (width/2) * math.cos(-0.53)), 
                int(P1[1] + (width/2) * math.sin(-0.53)))

        cv2.line(self.res, P1, P2, line_colour, line_px_width)
        cv2.line(self.res, P1, P3, line_colour, line_px_width)
        #cv2.line(self.res, (0, 0), (height, width), line_colour, 1)



    def stateCallback(self, data):
        self.grid = []
        for row in data.grid:
            self.grid.append([x for x in row.row])

        self.grid = np.asarray(self.grid, dtype=np.uint8)

        # Colour Representation
        bgr_img = np.zeros([self.grid.shape[0], self.grid.shape[1], 3], np.uint8)
        if 2 in self.grid:
            print("FOUND OBSTACLE! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        # Construct BGR colour channels
        # Must be divided by 255 because of scaling, and
        # converted to to float since they need to be int to index first
        bgr_img[:,:,0] = np.asarray(self.b_map[self.grid], dtype=np.uint8)
        bgr_img[:,:,1] = np.asarray(self.g_map[self.grid], dtype=np.uint8)
        bgr_img[:,:,2] = np.asarray(self.r_map[self.grid], dtype=np.uint8)
        
        
        #for row in range(self.grid.shape[0]):
            #for cell in range(self.grid.shape[1]):
                #cell_val = self.grid[row, cell]
                #(b, g, r) = COLOURS[cell_val]
                #bgr_img[row, cell, 0] = b
                #bgr_img[row, cell, 1] = g
                #bgr_img[row, cell, 2] = r

        res = cv2.resize(bgr_img, None, fx=self.image_scale, fy=self.image_scale, 
                            interpolation = cv2.INTER_AREA)

        # Publish to custom visualiser window
        cv2.imshow(self.window, res)
        cv2.waitKey(10)

        # Publish to RVIZ

    def makeImageMsg(self):




if __name__ == '__main__':
    try:
        CAVisualiser()
        rospy.spin()
    except Exception as e:
        raise e