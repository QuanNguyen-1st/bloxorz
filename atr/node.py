from atr.player import Player
from atr.player import DetachedPlayer
from atr.moves import Move
from atr.position import Position
import math
from collections import defaultdict

def printMapAsArr(arr: list):
    pass

class Node:
    def __init__(self, arr: list, player:Player, move: str, parent):
        self.arr = arr
        self.player = player
        self.move = move
        self.parent = parent

    def makePathTo(self) -> str:
        curr = self
        par = curr.parent
        string = ""
        while par is not None:
            if type(curr.player) == DetachedPlayer and type(par.player) == Player:
                string = str(curr.player) + " " + string
            string = str(curr.move) + " " + string
            curr = par
            par = par.parent
        return string
    
    def __str__(self) -> str:
        return str(self.player)
    
    def __eq__(self, __o: object) -> bool:
        return self.arr == __o.arr and self.player == __o.player

class BFS_Node(Node):
    def __init__(self, arr: list, player: Player, move: str, parent):
        super().__init__(arr, player, move, parent)

class A_star_Node(Node):
    def __init__(self, arr: list, player: Player, move: str, parent, g, h):
        super().__init__(arr, player, move, parent)
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, __o):
        return self.f < __o.f
    
class MC_Node(Node):
    def __init__(self, arr: list, player: Player, move: str, parent):
        super().__init__(arr, player, move, parent)
        self.N = 0
        self.Q = 0
        self.children = []

    def value(self, c_param = math.sqrt(2)):
        if self.N == 0:
            return float('inf')
        else:
            return self.Q/self.N + c_param*math.sqrt(math.log(self.parent.N) / self.N)


    # def isLoseState(self) -> bool:
    #     return not (self.arr[self.player.p1.x][self.player.p1.y] and self.arr[self.player.p2.x][self.player.p2.y])
    
    # def isWinState(self) -> bool:
    #     return self.player.isStanding() and self.player.p1 == self.goal
    
    # def isTerminalState(self) -> bool:
    #     return self.isWinState() or self.isLoseState()
    