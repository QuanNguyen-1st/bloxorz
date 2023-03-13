from atr.map import Map
from atr.player import Player
from atr.player import DetachedPlayer
from atr.position import Position
from atr.bfs import BFS
from atr.astar import AStar
import atr.button as bt

game = Map("bloxorz/level/28.txt")

# bfs = BFS(game)
# bfs.solve()
# print(bfs.winPath)

astar = AStar(game)
astar.solve()
print(astar.winPath)
