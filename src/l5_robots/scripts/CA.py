#!/usr/bin/env python


# This script constructs and returns an object that represents a
# 2D cellular automata using the rules from Conway's game of life.
# Constructs a new grid for every update.

import numpy as np
import time
import math
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from random import randint
import sys

import rospy
from l5_robots.msg import CaGrid, CaRow, Obstacles

HEIGHT = 40
WIDTH = 40
LIVE = 1
DEAD = 0
OBSTACLE = 2

OCTAGON_PATTERN = [ (0, 3), (0, 4), (1, 2), (1, 5), 
            (2, 1), (2, 6), (3, 0), (3, 7), 
            (4, 0), (4, 7), (5, 1), (5, 6), 
            (6, 2), (6, 5), (7, 3), (7, 4) ]


# Takes LaserScan data and uses it to maintain a CA representing
# The robot's surroundings. It sends this data to the ca/state topic,
# where it can be used to take actions.
class CA():
    def __init__(self):
        self.octagonSet = False
        self.lat = np.zeros((HEIGHT, WIDTH), int)


        rospy.init_node('CA', anonymous=False)
        rospy.loginfo("CA node started.")
        rospy.on_shutdown(self.shutdown)
        
        if (HEIGHT % 2 == 1) or (WIDTH % 2 == 1):
            rospy.loginfo("ERROR: Odd number of cells for h & w. Should be even to keep the robot in the centre.")
            sys.exit(0)
        elif (HEIGHT < 10) or (WIDTH < 10):
            rospy.loginfo("ERROR: Height & width too small. Minimum 10.")
            sys.exit(0)

        try:
            rospy.Subscriber("ca/obstacles", Obstacles, self.obstaclesCallback)
        except Exception as e:
            print(e)
            sys.exit(0)

        try:
            self.state_pub = rospy.Publisher('ca/state', CaGrid, queue_size=10)
            r = rospy.Rate(10);
        except Exception as e:
            print(e)
            sys.exit(0)

        while not rospy.is_shutdown():
            r.sleep()
    

    # Given a cell, check it's Moore neighbours, return a sum of live ones
    # Functions by adding all live cells found within a size 9 kernel, except the centre
    def checkNeighbours(self, i, j):
        check_range = [-1, 0, 1]
        res = 0

        for y_offset in check_range:
            y = i + y_offset 
            if y < 0 or y >= HEIGHT:
                continue

            for x_offset in check_range:
                if y_offset == 0 and x_offset ==0:
                    continue

                x = j + x_offset
                if x < 0 or x >= WIDTH:
                    continue
                
                if self.lat[y][x] == LIVE:
                    res = res + 1

        return res

    # TODO: More pythonic way of implementing?
    def update(self):
        # If oscillator is not set, set it
        if not self.octagonSet:
            self.setOctagon()
            self.octagonSet = True

        newLattice = np.zeros((HEIGHT, WIDTH), int)

        # Count the state of the neighbours, then update according to Brian's Brain rules
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if self.lat[i][j] == OBSTACLE:
                    newLattice[i][j] = OBSTACLE
                    continue

                neighbour_sum = self.checkNeighbours(i, j)

                # GAME OF LIFE RULES
                if self.lat[i][j] == LIVE:
                    if (neighbour_sum < 2) or (neighbour_sum > 3):
                        newLattice[i][j] = DEAD
                    else:
                        newLattice[i][j] = LIVE # Because the newLattice is init'ed with 0's - this case is required
                elif self.lat[i][j] == DEAD:
                    if neighbour_sum == 3:
                        newLattice[i][j] = LIVE

                # BRIAN'S BRAIN RULES
                #if (lat[i][j] == DEAD) and (neighbour_sum == 2):   # Cell is dead
                #    newLattice[i][j] = LIVE
                #elif (lat[i][j] == LIVE):  # Cell is live
                #    newLattice[i][j] = BETWEEN
                #if (self.lat[i][j] == BETWEEN): # Betweens again eligible for life
                #    newLattice[i][j] = DEAD

        self.lat = newLattice


    def setStates(self):
        if (len(lat) != len(array)) or (len(lat[0]) != len(array[0])):
            print("Error: setStatesArray() - array lengths don't match")

        for i in range(HEIGHT):
            for j in range(WIDTH):
                lat[i][j] = array[i][j]


    def randomise(self):
        self.lat = np.random.choice([1, 0], len(self.lat) * len(self.lat[0]), p=[0.1, 0.9]).reshape(len(self.lat), len(self.lat[0]))


    def validate(self):
        accepted = [LIVE, DEAD, OBSTACLE]
        for y in lat:
            for x in y:
                if not x in accepted:
                    print("ERROR: Value error - Domains not respected")

    # Sets the octagon oscillator in the centre of the CA
    def setOctagon(self):
        rel_x = (WIDTH/2) - 4
        rel_y = (HEIGHT/2) - 4
        for y in range(8):
            for x in range(8):
                if (x, y) in OCTAGON_PATTERN:
                    self.lat[rel_y + y][rel_x + x] = LIVE
                else:
                    self.lat[rel_y + y][rel_x + x] = DEAD

    # Sets the spinner oscillator in the centre of the CA
    def setSpinner(self):
        x = WIDTH/2
        y = HEIGHT/2

        self.lat[y][x] = LIVE
        self.lat[y-1][x] = LIVE
        self.lat[y+1][x] = LIVE


    # Calculates the locations of the obstacles and picks the correct CA cell.
    # The CA is considered a local map with the robot in the center.
    # This is the main loop function, it calls update() and publish()
    def obstaclesCallback(self, data):
        obstacles = []
        cell_height = data.max_range / ((HEIGHT ) / 2)
        cell_width = data.max_range / ((WIDTH) / 2)

        # Reset obstacle cells in the CA to 0 (for refreshing locations)
        self.lat[self.lat == OBSTACLE] = DEAD

        for d, a in zip(data.distances, data.angles):
            x = d * math.cos(a)
            y = d * math.sin(a)

            # How many cells away from the robot
            x_cell = int(math.floor(x / cell_width))
            y_cell = int(math.floor(y / cell_height))

            # Which cell, from the centre
            x_cell = ((WIDTH) / 2) + x_cell
            y_cell = ((HEIGHT) / 2) - y_cell

            # Fill in that cell
            self.lat[y_cell, x_cell] = OBSTACLE
            #print("Filled in: " + str(y_cell) + " " + str(x_cell))

        self.update()
        self.publishState()


    # Publish the CA as a CAGrid msg (custom msg file)
    def publishState(self):
        grid = []

        for x in self.lat:
            r = CaRow()
            r.row = x
            grid.append(r)

        grid_msg = CaGrid()
        grid_msg.grid = grid

        self.state_pub.publish(grid_msg)


    # STUB
    def display(self):
        print(lat)


    def shutdown(self):
        rospy.loginfo("CA node shutting down..")
        rospy.sleep(1)




if __name__ == "__main__":
    try:
        CA()
    except Exception as e:
        raise e
