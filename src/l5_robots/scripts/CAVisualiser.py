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
from cv_bridge import CvBridge, CvBridgeError
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
        self.image_res = 600
        self.info_panel_height = 150
        self.border_thickness = 3

        # Construct nunpy arrays used to convert 2D grayscale to 3D BGR
        self.b_map = np.array([COLOURS[mapping][0] for mapping in COLOURS])
        self.g_map = np.array([COLOURS[mapping][1] for mapping in COLOURS])
        self.r_map = np.array([COLOURS[mapping][2] for mapping in COLOURS])

        # Used to create ROS Image to publish
        self.bridge = CvBridge()
               
        try:
            rospy.Subscriber("ca/state", CaGrid, self.stateCallback)
        except Exception as e:
            print(e)
            sys.exit(0)

        try:
            self.img_pub = rospy.Publisher("ca/internal_img_rgb", Image, queue_size=10)
        except Exception as e:
            print(e)
            sys.exit(0)


    def shutdown(self):
        rospy.loginfo("CAVisualiser node shutting down.")
        cv2.destroyAllWindows()

    # Draws lines to tell where laserscanner reaches
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

    # Returns an OpenCV image with an info panel below
    def addInfoPanel(self):
        s = self.res.shape
        # Create new array with extra space
        img = np.ones([s[0] + self.info_panel_height, s[1], s[2]], dtype=np.uint8)

        # Copy over the image data
        img[:s[0],:,:] = self.res

        #Give the panel a colour
        img[s[0]:,:] = (0, 0, 255) 
        img[s[0]+self.border_thickness:,:] = (255, 255, 245)
        return img


    def stateCallback(self, data):
        self.grid = []
        for row in data.grid:
            self.grid.append([x for x in row.row])

        self.grid = np.asarray(self.grid, dtype=np.uint8)

        # Colour Representation
        bgr_img = np.zeros([self.grid.shape[0], self.grid.shape[1], 3], dtype=np.uint8)

        # Construct BGR colour channels
        # Must be divided by 255 because of scaling, and
        # converted to to float since they need to be int to index first
        bgr_img[:,:,0] = np.asarray(self.b_map[self.grid], dtype=np.uint8)
        bgr_img[:,:,1] = np.asarray(self.g_map[self.grid], dtype=np.uint8)
        bgr_img[:,:,2] = np.asarray(self.r_map[self.grid], dtype=np.uint8)
        
        # Old slow code - educational
        #for row in range(self.grid.shape[0]):
            #for cell in range(self.grid.shape[1]):
                #cell_val = self.grid[row, cell]
                #(b, g, r) = COLOURS[cell_val]
                #bgr_img[row, cell, 0] = b
                #bgr_img[row, cell, 1] = g
                #bgr_img[row, cell, 2] = r

        scaling_factor = self.image_res / bgr_img.shape[0]

        self.res = cv2.resize(bgr_img, None, fx=scaling_factor, fy=scaling_factor, 
                            interpolation = cv2.INTER_AREA)

        # Publish to custom visualiser window
        cv2.imshow(self.window, self.addInfoPanel())
        cv2.waitKey(10)

        # Publish Image
        self.img_pub.publish(self.bridge.cv2_to_imgmsg(self.res))


if __name__ == '__main__':
    try:
        CAVisualiser()
        rospy.spin()
    except Exception as e:
        raise e