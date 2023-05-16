""" EightPuzzleWithManhattan.py

Manhattan Heuristic for Eight Puzzle Problem
Partnership? (YES or NO): Yes
Student Name 1: Joseph Leuschen
Student Name 2: Hritik Arasu

UW NetID Student 1: jleusche
UW NetID Student 2: harasu
CSE 415, Autumn 2022, University of Washington

This code contains my implementation of the manhattan heuristic for the eight puzzle problem

Usage:
python3 EightPuzzleWithManhattan.py
"""

import math
from EightPuzzle import *
init_state_list = [[3, 1, 2], [0, 5, 8], [4, 6, 7]]

def h(s):
    optimal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def convertMatrix(board):
        newMatrix = []
        for i in range(3):
            for j in range(3):
                newMatrix.append(board[i][j])
        return newMatrix
    count = 0
    newMatrix = convertMatrix(s.b)
    for i in range(len(newMatrix)):
        diff = abs(optimal.index(newMatrix[i]) - newMatrix.index(newMatrix[i]))
        if newMatrix[i] != 0:
            x = diff % 3
            y = diff / 3
            count += x + int(math.floor(y))
            if abs(optimal.index(newMatrix[i]) % 3 - newMatrix.index(newMatrix[i]) % 3) == 2 and diff % 3 == 1:
                count += 2
    return count