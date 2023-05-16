# import sys, importlib.util
# spec = importlib.util.spec_from_file_location("Farmer_Fox", "Farmer_Fox" + ".py")
# PROBLEM = spec.loader.load_module()
import math
# COMBOS = [1234, 1243, 1423, 4123, 1324, 1342, 1432, 4132, 3124, 3142, 3412, 4312, 2134, 2143, 2413, 4213, 2314, 2341, 2431, 4231, 3214, 3241, 3421, 4321]
# for i in range(len(COMBOS)):
#     COMBOS[i] = list(str(COMBOS[i]))
# for i in range(len(COMBOS)):
#     for j in range(4):
#         COMBOS[i][j] = int(COMBOS[i][j])
# print(COMBOS)

def h(s):
    count = 0
    for i in range(3):
        for j in range(3):
            if (3*i + j) != s[i][j]:
                count += 1
    return count

def findIndex(num, board):
    i = 0
    while num not in board[i]:
        i += 1
    j = board[i].index(num)
    return i*3 + j

def h(s):
    optimal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def convertMatrix(board):
        newMatrix = []
        for i in range(3):
            for j in range(3):
                newMatrix.append(board[i][j])
        return newMatrix
    count = 0
    newMatrix = convertMatrix(s)
    for i in range(len(newMatrix)):
        diff = abs(optimal.index(newMatrix[i]) - newMatrix.index(newMatrix[i]))
        if newMatrix[i] != 0:
            x = diff % 3
            y = diff / 3
            count += x + int(math.floor(y))
            if abs(optimal.index(newMatrix[i]) % 3 - newMatrix.index(newMatrix[i]) % 3) == 2 and diff % 3 == 1:
                count += 2
    return count

print(h([[3, 1, 2], [0, 5, 8], [4, 6, 7]]))