#!/usr/bin/env python

# Script to set all global parameters in the CA Hybrid Architecture


import rospy

#height, wdith, colours

rospy.set_param('HEIGHT', 40)

class SetParams():
    def __init__(self):
        rospy.init_node('CAInterpreter', anonymous=False)
        rospy.loginfo("Setting Parameters.")
        

        # Laser2Scan
        rospy.set_param('CALLBACK_TIME_FILTER', 0.03)
        rospy.set_param('LASER_RANGE_MAX', 5.0)


        # CA
        rospy.set_param('HEIGHT', 40)
        rospy.set_param('WIDTH', 40)
        rospy.set_param('LIVE', 1)
        rospy.set_param('DEAD', 0)
        rospy.set_param('OBSTACLE', 2)  
        rospy.set_param('OCTAGON_PATTERN', [ (0, 3), (0, 4), (1, 2), (1, 5), 
                    (2, 1), (2, 6), (3, 0), (3, 7), 
                    (4, 0), (4, 7), (5, 1), (5, 6), 
                    (6, 2), (6, 5), (7, 3), (7, 4) ])   
        

        # ROIs
        rospy.set_param('ROIl', [(20, 5), (5, 5)])
        rospy.set_param('ROIr', [(20, 5), (25, 5)])
        rospy.set_param('THRESH_LIMIT', 0.5)
        rospy.set_param('REFRESH_LIMIT', 400)


        rospy.on_shutdown(self.shutdown)


    def shutdown(self):
        rospy.loginfo("Parameters set. Exiting.")


if __name__ == '__main__':
    try:
        SetParams()
    except Exception as e:
        raise e
        print(e)