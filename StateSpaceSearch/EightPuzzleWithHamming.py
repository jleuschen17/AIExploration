""" EightPuzzleWithHamming.py

Hamming Heuristic for Eight Puzzle Problem
Partnership? (YES or NO): Yes
Student Name 1: Joseph Leuschen
Student Name 2: Hritik Arasu

UW NetID Student 1: jleusche
UW NetID Student 2: harasu
CSE 415, Autumn 2022, University of Washington

This code contains my implementation of the hamming heuristic for the eight puzzle problem

Usage:
python3 EightPuzzleWithHamming.py
"""
from EightPuzzle import *

init_state_list = [[3, 1, 2], [0, 5, 8], [4, 6, 7]]

def h(s):
    count = 0
    for i in range(3):
        for j in range(3):
            if (3*i+j) != s.b[i][j] and s.b[i][j] != 0:
                count += 1
    return count