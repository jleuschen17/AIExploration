'''
Name(s):
UW netid(s):
'''

from game_engine import genmoves

class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class BackgammonPlayer:
    def __init__(self):
        def staticEval(state):
            pointlist = state.pointLists
            pipWhite = 0
            pipBlack = 0
            total = 0
            for i in range(len(pointlist)):
                for j in range(len(pointlist[i])):
                    if pointlist[i][j] == 0:
                        pipWhite += i
                        if i >= 19:
                            total += 75
                        elif i >= 13:
                            total += 35
                        elif i >= 7:
                            total += 10
                    else:
                        pipBlack += 23 - i
                        if i <= 6:
                            total -= 75
                        elif i <= 13:
                            total -= 35
                        elif i <= 19:
                            total -= 10
            total += 3*(pipBlack - pipWhite)
            for i in range(len(state.bar)):
                if state.bar[i] == 0:
                    total -= 30
                else:
                    total += 30
            total -= 100*(len(state.red_off))
            total += 100*(len(state.white_off))
            return total



        self.staticEvalFunc = staticEval
        self.GenMoveInstance = genmoves.GenMoves()
        self.maxPly = 2
        self.currVals = []
        # feel free to create more instance variables as needed.

    # TODO: return a string containing your UW NETID(s)
    # For students in partnership: UWNETID + " " + UWNETID
    def nickname(self):
        # TODO: return a string representation of your UW netid(s)
        return "harasu jleusche"

    def introduce(self):
        return"I\'m dsbg"

    def initialize_move_gen_for_state(self, state, who, die1, die2):
        self.move_generator =  self.GenMoveInstance.gen_moves(state, who, die1, die2)

    # If prune==True, then your Move method should use Alpha-Beta Pruning
    # otherwise Minimax
    def useAlphaBetaPruning(self, prune=False):
        # TODO: use the prune flag to indiciate what search alg to use
        return prune
    # Returns a tuple containing the number explored
    # states as well as the number of cutoffs.
    def statesAndCutoffsCounts(self):
        # TODO: return a tuple containig states and cutoff
        return (-1, -1)

    # Given a ply, it sets a maximum for how far an agent
    # should go down in the search tree. maxply=2 indicates that
    # our search level will go two level deep.
    def setMaxPly(self, maxply=3):
        self.maxPly = maxply

    # If not None, it update the internal static evaluation
    # function to be func
    def useSpecialStaticEval(self, func):
        self.staticEvalFunc = func

    # Given a state and a roll of dice, it returns the best move for
    # the state.whose_move.
    # Keep in mind: a player can only pass if the player cannot move any checker with that role
    def move(self, state, die1=1, die2=6):
        root = TreeNode(state, [])
        self.buildTree(root, die1, die2, self.maxPly)
        self.currVals = []
        valsRoot = TreeNode(None, [])
        self.moveDown(root, valsRoot)
        while type(valsRoot.children[0]) != int:
            self.calcVals(valsRoot, 0)
        maxVal = max(filter(lambda x: x is not None, valsRoot.children))
        print(valsRoot.children)
        maxValIndex = valsRoot.children.index(maxVal)
        self.initialize_move_gen_for_state(state, state.whose_move, die1, die2)
        moves = self.get_all_moves()
        print("Choice: ", moves[maxValIndex][0])
        return moves[maxValIndex][0]




    def buildTree(self, root, die1, die2, maxPly):
        if maxPly > 0:
            for child in self.calcMoves(root.val, die1, die2):
                try:
                    root.children.append(TreeNode(child[1], []))
                except:
                    pass
        for child in root.children:
            self.buildTree(child, die1, die2, maxPly - 1)


    def calcMoves(self, state, die1, die2):
        if type(state) != tuple:
            self.initialize_move_gen_for_state(state, state.whose_move, die1, die2)
            move_lists = self.get_all_moves()
        else:
            move_lists = []
        return move_lists

    def moveDown(self, root, valsRoot):
        if root.children:
            if len(root.children[0].children) == 0:
                for child in root.children:
                    valsRoot.children.append(self.staticEvalFunc(child.val))
            else:
                for child in root.children:
                    valsRoot.children.append(TreeNode(None, []))
                for i in range(len(root.children)):
                    self.moveDown(root.children[i], valsRoot.children[i])
        else:
            return

    def calcVals(self, valsRoot, minMax):
        if type(valsRoot.children[0].children[0]) == int:
            for i in range(len(valsRoot.children)):
                try:
                    if minMax == 1:
                        temp = max(filter(lambda x: x is not None, valsRoot.children[i].children))
                        valsRoot.children[i] = temp
                    else:
                        temp = min(filter(lambda x: x is not None, valsRoot.children[i].children))
                        valsRoot.children[i] = temp
                except:
                    valsRoot.children[i] = None
        else:
            for child in valsRoot.children:
                if minMax == 1:
                    self.calcVals(child, 0)
                else:
                    self.calcVals(child, 1)
    def get_all_moves(self):
        """Uses the mover to generate all legal moves."""
        move_list = []
        done_finding_moves = False
        any_non_pass_moves = False
        while not done_finding_moves:
            try:
                m = next(self.move_generator)    # Gets a (move, state) pair.
                # print("next returns: ",m[0]) # Prints out the move.    For debugging.
                if m[0] != 'p':
                    any_non_pass_moves = True
                    move_list.append(m)    # Add the move to the list.
            except StopIteration as e:
                done_finding_moves = True
        if not any_non_pass_moves:
            move_list.append('p')
        return move_list

    def staticEval(self, state):
        return self.staticEvalFunc(state)
    # Hint: Look at game_engine/boardState.py for a board state properties you can use.
    # def staticEval(self, state):
    #     pointlist = state.pointLists
    #     pipWhite = 0
    #     pipBlack = 0
    #     for i in range(len(pointlist)):
    #         for j in range(len(pointlist[i])):
    #             if pointlist[i][j] == 0:
    #                 pipWhite += i
    #             else:
    #                 pipBlack += 23 - i
    #     return pipWhite - pipBlack

#
#
# if __name__ == "__main__":
#     player = BackgammonPlayer()
#     state = bgstate()
#     player.setMaxPly(3)
#     print(player.move(state))