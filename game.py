from atr.map import Map
from atr.player import Player
from atr.player import DetachedPlayer
from atr.position import Position
from atr.bfs import BFS
import atr.button as bt

game = Map("bloxorz/level/01.txt")
solve = BFS(game)
print(solve.BFS_solve())

# a = DetachedPlayer(Position(1,1), Position(2,2)) 
# print(type(a) == Player)
