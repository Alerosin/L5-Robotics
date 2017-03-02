#!/usr/bin/env python

# Listens to /ca/state, visualises the grid

import rospy
from l5_robots.msg import CaGrid, CaRow, InterpreterData
import numpy as np
import math
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import Header
from cv_bridge import CvBridge, CvBridgeError
import sys

# Colour mappings in BGR
COLOURS = rospy.get_param('colour_mappings')
COLOURS = {int(k):eval(v) for k,v in COLOURS.items()}

# ROI's in format: [(starting x coord, x length), (starting y coord, y length)]
ROIl = rospy.get_param('ROIl')
ROIr = rospy.get_param('ROIr')

# Convert from list of lists to list of tuples
ROIl = [(int(x[0]), int(x[1])) for x in ROIl]
ROIr = [(int(x[0]), int(x[1])) for x in ROIr]


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
        self.info_dict = {
                    "ROIl_ratio": 0,
                    "ROIl_thresh": 0,
                    "ROIr_ratio": 0,
                    "ROIr_thresh": 0,
                    "thresh_limit": 0,
                    "refresh_counter": 0,
                    "refresh_limit": 0,
                    "action": 0
        }

        # Construct nunpy arrays used to convert 2D grayscale to 3D BGR
        self.b_map = np.array([COLOURS[mapping][0] for mapping in COLOURS])
        self.g_map = np.array([COLOURS[mapping][1] for mapping in COLOURS])
        self.r_map = np.array([COLOURS[mapping][2] for mapping in COLOURS])

        # Used to create ROS Image to publish
        self.bridge = CvBridge()
               
        try:
            rospy.Subscriber("ca/state", CaGrid, self.stateCallback)
            rospy.Subscriber("ca/interpreter_data", InterpreterData, self.infoCallback)
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

    def drawROIs(self, scaling_factor):
        for r in (ROIl, ROIr):
            x = r[0][0] * scaling_factor
            x2 = (r[0][0] + r[0][1]) * scaling_factor

            y = r[1][0] * scaling_factor
            y2 = (r[1][0] + r[1][1]) * scaling_factor

            cv2.rectangle(self.res, (x, y), (x2, y2), (255, 0, 0), 1)



    # Returns an OpenCV image with an info panel below
    def addInfoPanel(self):
        s = self.res.shape
        font = 2
        font_size = 1
        font_c = (0, 0, 0)
        # Create new array with extra space
        img = np.ones([s[0] + self.info_panel_height, s[1], s[2]], dtype=np.uint8)

        # Copy over the image data
        img[:s[0],:,:] = self.res

        #Give the panel a colour
        img[s[0]:,:] = (0, 0, 255) 
        img[s[0]+self.border_thickness:,:] = (255, 255, 245)

        t_pad = 10
        t_space = t_pad + font_size * 25
        bot_y = img.shape[0] - t_pad
        left_x = t_pad

        lR = "Left Ratio: " + str(self.info_dict['ROIl_ratio']) + "/" + str(self.info_dict['thresh_limit'])
        #lT = " Left Threshold: " + str(self.info_dict['ROIl_thresh'])
        rR = "Right Ratio: " + str(self.info_dict['ROIr_ratio']) + "/" + str(self.info_dict['thresh_limit'])
        #rT = "Right Threshold: " + str(self.info_dict['ROIr_thresh'])
        
        if self.info_dict['ROIl_ratio'] > self.info_dict['thresh_limit']:
            col_l = (250, 0, 0)
        else:
            col_l = (0, 0, 0)

        if self.info_dict['ROIr_ratio'] > self.info_dict['thresh_limit']:
            col_r = (250, 0, 0)
        else:
            col_r = (0, 0, 0)

        print("PUT TEXT")
        cv2.putText(img, lR, (left_x, bot_y - t_space*3), font, font_size, col_l)
        cv2.putText(img, rR, (left_x, bot_y - t_space*2), font, font_size, col_r)

        cv2.putText(img, "Action: " + str(self.info_dict['action']), (left_x, bot_y - t_space), font, font_size, font_c)
        ref_t = "Refresh Counter: " + str(self.info_dict['refresh_counter'])+ "/" + str(self.info_dict['refresh_limit'])
        cv2.putText(img, ref_t, (left_x, bot_y), font, font_size, font_c)
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
        
        self.drawROIs(scaling_factor)

        # Publish Image
        self.img_pub.publish(self.bridge.cv2_to_imgmsg(self.res))

        
        # Publish to custom visualiser window
        self.img = self.addInfoPanel()
        cv2.imshow(self.window, self.img)
        cv2.waitKey(10)

    def infoCallback(self, data):
        self.info_dict['ROIl_ratio'] = data.ROIl_ratio
        self.info_dict['ROIl_thresh'] = data.ROIl_thresh
        self.info_dict['ROIr_ratio'] = data.ROIr_ratio
        self.info_dict['ROIr_thresh'] = data.ROIr_thresh
        self.info_dict['thresh_limit'] = data.thresh_limit
        self.info_dict['refresh_counter'] = data.refresh_counter
        self.info_dict['refresh_limit'] = data.refresh_limit
        self.info_dict['action'] = data.action
        


if __name__ == '__main__':
    try:
        CAVisualiser()
        rospy.spin()
    except Exception as e:
        raise e