from atr.map import Map
from atr.bfs import BFS
from atr.astar import AStar
from atr.monte_carlo import MCTS
from atr.algorithm import Algorithm
import time
from OpenGL.GL import *
from OpenGL.GLU import *
import os, psutil

def count_steps(path):
    count = 0
    for step in path:
        if "Up" in step or "Down" in step or "Left" in step or "Right" in step:
            count += 1
    return count

class Game:
    def __init__(self, level):
        self.level = level
        temp_str = "level/" + level + ".txt" 
        self.game = Map(temp_str)

    def solve_with_algorithm(self, algorithm):
        process = psutil.Process(os.getpid())
        temp_memory = process.memory_info().rss / 1024 / 1024
        start_time = time.time()

        if (algorithm == Algorithm.BFS):
            game_to_solve = BFS(self.game)
            game_to_solve.solve()
        elif (algorithm == Algorithm.ASTAR):
            game_to_solve = AStar(self.game)
            game_to_solve.solve()
        elif (algorithm == Algorithm.MCTS):
            game_to_solve = MCTS(self.game)
            game_to_solve.solve()

        print(self.level, time.time() - start_time, end = ' ')

        winPath = game_to_solve.winPath
        self.solution = list(winPath.split(" "))
        print(process.memory_info().rss / 1024 / 1024 - temp_memory, count_steps(self.solution), game_to_solve.VNode_count)
