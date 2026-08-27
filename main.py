# Ethan Davison
# CSCI 446 Fall 2026
# Programming Assignment #1
# I declare that I am the author of this work, take full responsibility for it, and have disclosed any material external assistance.

import random

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

    def printGrid(self):
        for i in self.grid:
            for j in i:
                print(j, end = " ")
            print("")
        print("")

    def dirtyGrid(self):
        for i in range(self.x):
            for j in range(self.y):
                # MAKE RANDOM DIRTYING STUFF HERE
                meow = 0

def moveVacuum(tempVacuum):
    meow = 0

def main():
    gridLength = 5
    gridHeight = 5
    
    grid = Grid(gridLength, gridHeight)
    grid.dirtyGrid()
    grid.printGrid()
    
    vacuum = [0,0]
    
    grid.printGrid()

main()