from atr.node import MC_Node
from atr.player import Player
from atr.map import Map
import math
import random
import copy
import numpy as np

class MCTS:
    winPath = ""
    VNode_count = 1
    can_find_win_path = True
    def __init__(self, map: Map):
        self.map = map

    def isWinState(self, player: Player):
        return player.isStanding() and player.p1 == self.map.goal

    def isLoseState(self, player: Player, arr: list):
        return not self.map.canHold(player, arr)

    def isTerminalState(self, player: Player, arr: list):
        return self.isWinState(player) or self.isLoseState(player, arr)
    
    def makeMoves(self, player: Player, arr: list, expanded: list):
        moves = self.map.legalMoves(player, arr)
        return [(playerMove, move, newMap) for (playerMove, move, newMap) in moves if (playerMove, newMap) not in expanded]
    
    def expand(self):
        pass

    def rollout(self):
        pass

    def back_propagate(self):
        pass

    def best_action(self):
        pass
