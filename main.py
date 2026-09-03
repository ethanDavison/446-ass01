# Ethan Davison
# CSCI 446 Fall 2026
# Programming Assignment #1
# I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.

import random
import time

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        grid = []
        for i in range(self.x):
            grid.append([])
            for j in range(self.y):
                grid[i].append(0)
        self.grid = grid
        self.vacuum = [0,0]

    def printGrid(self):
        for i in range(self.x):
            for j in range(self.y):
                if self.vacuum == [i,j]:
                    print("V", end = " ")
                else:
                    print(self.grid[i][j], end = " ")
            print("")
        print("")

    def dirtyGrid(self):
        for i in range(self.x):
            for j in range(self.y):
                if random.randint(0,1) == 0:
                    self.grid[i][j] = "x"

    def moveVacuum(self):
        direction = random.randint(1,4)
        if direction == 1 and self.vacuum[1] != 0:
            self.vacuum[1] -= 1
        elif direction == 2 and self.vacuum[0] != self.x-1:
            self.vacuum[0] += 1
        elif direction == 3 and self.vacuum[1] != self.y-1:
            self.vacuum[1] += 1
        elif direction == 4 and self.vacuum[0] != 0:
            self.vacuum[0] -= 1
        else:
            self.moveVacuum()
    
    def startCleaning(self):
        while True:
            self.printGrid()
            [vx,vy] = self.vacuum
            if self.grid[vx][vy] == "x":
                self.grid[vx][vy] = "0"
            self.moveVacuum()
            time.sleep(1)
            

def main():
    gridLength = 5
    gridHeight = 5
    
    grid = Grid(gridLength, gridHeight)
    grid.dirtyGrid()
    
    grid.startCleaning()

main()
