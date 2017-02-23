#!/usr/bin/env python

# Read input from laser scanner on /scan
# Convert into input for the CA

import math
import rospy
from sensor_msgs.msg import LaserScan
from l5_robots.msg import Obstacles

CALLBACK_TIME_FILTER = rospy.Duration(0.03) # Time between read /scan messages, in nanoseconds
LASER_RANGE_MAX = 5.0 # Max desired range for laser scanner, should be shorter than physical range limit of scanner

class Laser2CA():
    # Get scan message and parse it - but only if the message 
    # is CALLBACK_TIME_FILTER older than the previously processed one. (i.e. a time filter)
    #   TODO: Add interpolation using time between measurements
    def scanCallback(self, data):
        if (data.header.stamp - self.stamp > CALLBACK_TIME_FILTER):
            self.stamp = data.header.stamp
            scanAngle = data.angle_min
            distances = []
            angles = []
            
            # Creates a list of tuples containing each 
            # range measurement and the angle it was captured at.            
            for x in data.ranges:
                # Filter noisy measurements (i.e. outside allowed range)
                if (x >= data.range_min) and (x <= LASER_RANGE_MAX):
                    distances.append(x)
                    angles.append(scanAngle)
                scanAngle += data.angle_increment

            obs = Obstacles()
            obs.distances = distances
            obs.angles = angles
            obs.max_range = LASER_RANGE_MAX
            self.obstacles_pub.publish(obs)


    def __init__(self):
        rospy.init_node('Laser2CA', anonymous=False)
        rospy.loginfo("Laser2CA node started.")
        rospy.on_shutdown(self.shutdown)
               
        self.scanData = ""
        try:
            rospy.Subscriber("/scan", LaserScan, self.scanCallback)
        except Exception as e:
            print(e)
            sys.exit(0)

        try:
            self.obstacles_pub = rospy.Publisher('ca/obstacles', Obstacles, queue_size=10)
            r = rospy.Rate(10);
        except Exception as e:
            print(e)
            sys.exit(0)

        self.stamp = rospy.Time.now()

        while not rospy.is_shutdown():
            r.sleep()


    def shutdown(self):
        rospy.loginfo("Stopping Laser2CA node..")
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        Laser2CA()
    except:
        rospy.loginfo("Laser2CA node terminated.")