from atr.player import Player
from atr.player import DetachedPlayer
from atr.moves import Move
from atr.position import Position

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
    
    # def __str__(self) -> str:
    #     return str(self.player) 

class BFS_Node(Node):
    def __init__(self, arr: list, player: Player, move: str, parent):
        super().__init__(arr, player, move, parent)