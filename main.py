# Ethan Davison
# CSCI 446 Fall 2026
# Programming Assignment #1
# I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.

import random
import time

class Grid:
    # Grid(int, int): Grid is made of size x by y, makes an included Vacuum
    def __init__(self, x, y):
        self.x = x
        self.y = y
        grid = []
        for i in range(self.x):
            grid.append([])
            for j in range(self.y):
                grid[i].append(0)
        self.dirtyCount = 0
        self.grid = grid
        self.vacuum = self.Vacuum(self)
    
    class Vacuum:
        # Vacuum(grid): Vacuum is made at a random x and y within the Grid
        def __init__(self, grid):
            self.grid = grid
            self.vx = random.randint(0, self.grid.x - 1)
            self.vy = random.randint(0, self.grid.y - 1)
            self.actCount = 0
        
        # moveRand(): Moves the vacuum randomly in one of four directions
        def moveRand(self):
            direction = random.randint(1,4)
            if direction == 1 and self.vy != 0:
                self.vy -= 1
            elif direction == 2 and self.vx != self.grid.x-1:
                self.vx += 1
            elif direction == 3 and self.vy != self.grid.y-1:
                self.vy += 1
            elif direction == 4 and self.vx != 0:
                self.vx -= 1
            else:
                self.moveRand()
                return
            self.actCount += 1
        
        # checkIfDirty(): Returns True if the Vacuum's spot is dirty
        def checkIfDirty(self):
            if self.grid.grid[self.vx][self.vy] == "x":
                return True
            else:
                return False
        
        # cleanSpot(int, int): Cleans the given position
        def cleanSpot(self, tempX, tempY):
            self.grid.grid[tempX][tempY] = "0"
            self.actCount += 1
            self.grid.dirtyCount -= 1
        
        # startCleaning(): Loops through printing the grid, cleaning the vacuum point, and moving the vacuum
        def startCleaning(self):
            while True:
                self.grid.printGrid()
                if self.grid.dirtyCount == 0:
                    break
                if self.checkIfDirty():
                    self.cleanSpot(self.vx, self.vy)
                else:
                    self.moveRand()
                time.sleep(1)
            print("Done!")
    
    # printGrid(): Prints the grid to a cleared console with Vacuum's action count
    def printGrid(self):
        print("\033[H\033[J", end="")
        print("Action Count:", self.vacuum.actCount)
        print("Dirty Spots Left:", self.dirtyCount)
        for i in range(self.x):
            for j in range(self.y):
                if [self.vacuum.vx,self.vacuum.vy] == [i,j]:
                    print("V", end = " ")
                else:
                    print(self.grid[i][j], end = " ")
            print("")
        print("")

    # dirtyGrid(): Randomly puts x's to dirty the grid
    def dirtyGrid(self):
        for i in range(self.x):
            for j in range(self.y):
                if random.randint(0,1) == 0:
                    self.grid[i][j] = "x"
                    self.dirtyCount += 1

def main():
    gridLength = 5
    gridHeight = 5
    
    grid = Grid(gridLength, gridHeight)
    grid.dirtyGrid()
    
    grid.vacuum.startCleaning()

main()
