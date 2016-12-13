
# This script constructs and returns an object that represents a
# 2D cellular automata using the rules from Conway's game of life.

import numpy as np

class CA:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.lattice = np.zeros((height, width), int)

    def update(self):
        lattice = self.lattice
        width = self.width
        height = self.height

        for i in range(height):
            for j in range(width):
                neighbour_sum = (lattice[i, (j-1)%width] + lattice[i, (j+1)%width] + lattice[(i-1)%height, j] + 
                            lattice[(i+1)%height, j] + lattice[(i-1)%height, (j-1)%width] +
                            lattice[(i-1)%height, (j+1)%width] + lattice[(i+1)%height, (j-1)%width] +
                            lattice[(i+1)%height, (j+1)%width])

                newLattice = np.zeros((height, width), int)

                if (lattice[i][j] == 1):
                    if (neighbour_sum == 3):
                        newLattice[i][j] = 1

        self.lattice = newLattice

    def setStates(self, array):
        #TODO: Set lattice to this array, implement error checking
        print("TODO")

    def randomise(self):
        #TODO: Randomise the cell states
        print("TODO")

    def validate(self):
        for y in self.lattice:
            for x in y:
                if (x != 0) and (x != 1):
                    print("ERROR: Element domains not respected")

    def display(self):
        print(self.lattice)



if __name__ == "__main__":
    ca = CA(4,5)
    ca.display()