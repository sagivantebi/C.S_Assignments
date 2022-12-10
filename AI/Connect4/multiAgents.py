"""
Introduction to Artificial Intelligence, 89570, Bar Ilan University, ISRAEL

Student name: Sagiv Antebi
Student ID: 318159282

"""

# multiAgents.py
# --------------
# Attribution Information: part of the code were created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# http://ai.berkeley.edu.
# We thank them for that! :)


import random, util, math

from connect4 import Agent


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxAgent, AlphaBetaAgent & ExpectimaxAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 1  # agent is always index 1
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class BestRandom(MultiAgentSearchAgent):

    def getAction(self, gameState):
        return gameState.pick_best_move()


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 1)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.isWin():
        Returns whether or not the game state is a winning state for the current turn player

        gameState.isLose():
        Returns whether or not the game state is a losing state for the current turn player

        gameState.is_terminal()
        Return whether or not that state is terminal
        """

        "*** YOUR CODE HERE ***"
        childrens = {}

        # Creating a dict of the successors and call the specific function
        for op in gameState.getLegalActions(self.index):
            child = gameState.generateSuccessor(self.index, op)
            # switch the turn between players
            child.switch_turn(gameState.turn)
            childrens[op] = self.MinMax_Value(child, self.depth - 1)

        # Finding the max value in the dict
        max_value = max(childrens, key=childrens.get)
        return max_value

    def MinMax_Value(self, gameState, D):
        # Check if terminal - than return evaluation
        if gameState.is_terminal() or D == 0:
            return self.evaluationFunction(gameState)

        # get successors
        childrens = []
        for action in gameState.getLegalActions(self.index):
            childrens.append(gameState.generateSuccessor(self.index, action))

        # Checks if it's the AI turn
        if gameState.turn == 1:
            cur_max = -float("inf")
            for child in childrens:
                # switch the turn between players
                child.switch_turn(gameState.turn)
                v = self.MinMax_Value(child, D - 1)
                cur_max = max(cur_max, v)
            return cur_max
        # if it is NOT the AI turn
        else:
            cur_min = float("inf")
            for child in childrens:
                # switch the turn between players
                child.switch_turn(gameState.turn)
                v = self.MinMax_Value(child, D - 1)
                cur_min = min(cur_min, v)
            return cur_min


class AlphaBetaAgent(MultiAgentSearchAgent):
    def getAction(self, gameState):
        """
            Your minimax agent with alpha-beta pruning (question 2)
        """
        "*** YOUR CODE HERE ***"
        childrens = {}

        # Creating a dict of the successors and call the specific function
        for op in gameState.getLegalActions(self.index):
            child = gameState.generateSuccessor(self.index, op)
            child.switch_turn(gameState.turn)
            childrens[op] = self.Min_Value(child, self.depth - 1, -float("inf"), float("inf"))

        max_value = max(childrens, key=childrens.get)
        return max_value
        util.raiseNotDefined()

    def Max_Value(self, gameState, D, a, b):
        if gameState.is_terminal() or D == 0:
            return self.evaluationFunction(gameState)

        # get successors
        childrens = []
        for action in gameState.getLegalActions(self.index):
            childrens.append(gameState.generateSuccessor(self.index, action))

        for child in childrens:
            child.switch_turn(gameState.turn)
            a = max(a, self.Min_Value(child, D - 1, a, b))
            # if b < a  - cut the tree
            if b < a:
                return b
        return a

    def Min_Value(self, gameState, D, a, b):
        if gameState.is_terminal() or D == 0:
            return self.evaluationFunction(gameState)

        # get successors
        childrens = []
        for action in gameState.getLegalActions(self.index):
            childrens.append(gameState.generateSuccessor(self.index, action))

        for child in childrens:
            child.switch_turn(gameState.turn)
            b = min(b, self.Max_Value(child, D - 1, a, b))
            # if b < a  - cut the tree
            if b < a:
                return a
        return b


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        childrens = {}

        # Creating a dict of the successors and call the specific function
        for op in gameState.getLegalActions(self.index):
            child = gameState.generateSuccessor(self.index, op)
            child.switch_turn(gameState.turn)
            # True - Max | False - Exp
            childrens[op] = self.value(child, self.depth - 1, False)

        max_value = max(childrens, key=childrens.get)
        return max_value
        util.raiseNotDefined()

    def value(self, gameState, D, Max_or_Exp):
        if gameState.is_terminal() or D == 0:
            return self.evaluationFunction(gameState)

        if Max_or_Exp:
            return self.max_value(gameState, D)

        else:
            return self.exp_value(gameState, D)

    def max_value(self, gameState, D):
        childrens = []
        for action in gameState.getLegalActions(self.index):
            childrens.append(gameState.generateSuccessor(self.index, action))

        v = -float("inf")

        for child in childrens:
            child.switch_turn(gameState.turn)
            v = max(v, self.value(child, D - 1, False))
        return v

    def exp_value(self, gameState, D):
        childrens = []
        for action in gameState.getLegalActions(self.index):
            childrens.append(gameState.generateSuccessor(self.index, action))

        v = 0
        len_childrens = len(childrens)

        for child in childrens:
            child.switch_turn(gameState.turn)
            # calculates the percentage of the child - his part
            p = 1 / len_childrens
            v += p * self.value(child, D - 1, True)
        return v
