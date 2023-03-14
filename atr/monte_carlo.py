from atr.node import MC_Node
from atr.player import Player
from atr.map import Map

class MCTS:
    def __init__(self, map: Map):
        self.map = map

    def isWinState(self, player: Player):
        return player.isStanding() and player.p1 == self.map.goal

    def isLoseState(self, player: Player, arr: list):
        return not self.map.canHold(player, arr)
    
    def isTerminalState(self, player: Player, arr: list):
        return self.isWinState(player) or self.isLoseState(player, arr)

    def selection(self):
        pass

    def expansion(self):
        pass

    def simulation(self):
        pass

    def backpropagation(self):
        pass
