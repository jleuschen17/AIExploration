'''Farmer_Fox.py
by Joseph Leuschen
UWNetID: jleusche
Student number: 2162382

Assignment 2, in CSE 415, Autumn 2022.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''
#<METADATA>
SOLUTION_VERSION = "2.0"
PROBLEM_NAME = "Farmer, Fox Problem"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['J. Leuschen']
PROBLEM_CREATION_DATE = "09-OCT-2022"
# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.
MAPPINGS = {0: "Farmer", 1: "Chicken", 2: "Fox", 3: "Grain"}
FARMER = 0
CHICKEN = 1
FOX = 2
GRAIN = 3
# TRY MAKING FARMER ITS OWN KEY IN THE D DICTIONARY
# COMBOS = [1234, 1243, 1423, 4123, 1324, 1342, 1432, 4132, 3124, 3142, 3412, 4312, 2134, 2143, 2413, 4213, 2314, 2341, 2431, 4231, 3214, 3241, 3421, 4321]
# for i in range(len(COMBOS)):
#     COMBOS[i] = list(str(COMBOS[i]))
# for i in range(len(COMBOS)):
#     for j in range(4):
#         COMBOS[i][j] = int(COMBOS[i][j])
# COMBOVAL = 14
# FARMER = COMBOS[COMBOVAL][0] - 1
# FOX = COMBOS[COMBOVAL][1] - 1
# CHICKEN = COMBOS[COMBOVAL][2] - 1
# GRAIN = COMBOS[COMBOVAL][3] - 1

class State():
    def __init__(self, d=None):
        if d==None:
            d = [[1, 1, 1, 1], [0, 0, 0, 0]]
        self.d = d
    def __eq__(self, s2):
        for i in range(2):
            if self.d[i] != s2.d[i]:
                return False
        return True
    def __str__(self):
        p = self.d
        txt = "[["
        for i in self.d[0]:
            txt += str(i) + ", "
        txt = txt[:len(txt)-2]
        txt += "], ["
        for i in self.d[1]:
            txt += str(i) + ", "
        txt = txt[:len(txt)-2]
        txt += "]]"
        return txt

        # txt = f"\nPeople on Left: "
        # origLen = len(txt)
        # for i in range(4):
        #     if p[0][i] == 1:
        #         txt += MAPPINGS[i] + ", "
        # if len(txt) > origLen:
        #     txt = txt[:len(txt)-2]
        # txt += "\nPeople on Right: "
        # origLen = len(txt)
        # for i in range(4):
        #     if p[1][i] == 1:
        #         txt += MAPPINGS[i] + ", "
        # if self.d[0][0] == 1:
        #     txt += "\nThe boat is on the left side"
        # else:
        #     txt += "\nThe boat is on the left side"
        if len(txt) > origLen:
            txt = txt[:len(txt)-2]
        return txt

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        news = State({})
        news.d = [[], []]
        for i in range(4):
            news.d[0].append(self.d[0][i])
            news.d[1].append(self.d[1][i])
        return news

    def update(self, choice):
        def driver(choiceVal, news):
            if news[0][choiceVal] == 1:
                news[0][choiceVal] = 0
            else:
                news[0][choiceVal] = 1
            if news[1][choiceVal] == 1:
                news[1][choiceVal] = 0
            else:
                news[1][choiceVal] = 1
            return news
        newMove = self.copy()
        if choice != FARMER:
            newMove.d = driver(choice, newMove.d)
        newMove.d = driver(FARMER, newMove.d)
        return newMove


    def can_move(self, choice):
        potential = self.update(choice)
        for i in range(2):
            if potential.d[i][CHICKEN] == 1 and potential.d[i][FOX] == 1 and potential.d[i][FARMER] == 0 and potential.d[i][GRAIN] == 0:
                return False
            if potential.d[i][FARMER] == 1 and potential.d[i][FOX] == 0 and potential.d[i][CHICKEN] == 0 and potential.d[i][GRAIN] == 0:
                return False
        for i in range(2):
            if potential.d[i][CHICKEN] == 1 and potential.d[i][GRAIN] == 1 and potential.d[i][FARMER] == 0 and potential.d[i][FOX] == 0:
                return False
            # if potential.d[i][CHICKEN] == 0 and potential.d[i][GRAIN] == 0 and potential.d[i][FARMER] == 1 and potential.d[i][FOX] == 1:
            #     return False
        return True

    def move(self, choice):
        if choice not in [0, 1, 2, 3]:
            raise Exception("Not a Valid Choice")
        news = self.update(choice)
        return news

def goal_test(s):
    p = s.d
    return (p[1] == [1, 1, 1, 1])

def goal_message(s):
    return "Congratulations on successfully guiding the Farmer, Fox, Chicken, and Grain across the River!"

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf
    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

CREATE_INITIAL_STATE = lambda : State(d=[[1, 1, 1, 1], [0, 0, 0, 0]])

OPERATORS = [Operator(
    f"Cross the river with the {MAPPINGS[choice]} (Farmer always crosses)",
    lambda s, choiceVal=choice: s.can_move(choiceVal),
    lambda s, choiceVal=choice:s.move(choiceVal) )
    for (choice) in [0, 1, 2, 3]
]

GOAL_TEST = lambda s: goal_test(s)

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
