import sys
from enum import Enum
from game import Game
import os, psutil

class Algorithm(Enum):
    NONE = 0,
    BFS = 1,
    ASTAR = 2,
    MCTS = 3

def main(level, algorithm):
    game = Game(level)
    if algorithm == Algorithm.NONE:
        game.setup()
        game.runningPlay()
    else:
        if algorithm == Algorithm.BFS:
            pass
            game.solveBFS()
            game.setup()
            game.runningAI()
        elif algorithm == Algorithm.ASTAR:
            pass
            game.solveAStar()
            game.setup()
            game.runningAI()
        elif algorithm == Algorithm.MCTS:
            pass
            game.solveMCTS()
            game.setup()
            game.runningAI()
    process = psutil.Process(os.getpid())
    memory_to_draw = process.memory_info().rss / 1024 / 1024 - game.memory
    print("Memory used to draw pygame:", memory_to_draw, "MB")


if __name__== "__main__":
    if len(sys.argv) > 2:
        level = sys.argv[1]
        algorithm = sys.argv[2]
        if algorithm == "play": 
            main(level=level, algorithm = Algorithm.NONE)
        elif algorithm == "bfs":
            main(level=level, algorithm = Algorithm.BFS)
        elif algorithm == "astar":
            main(level=level, algorithm = Algorithm.ASTAR)
        elif algorithm == "mcts":
            main(level=level, algorithm = Algorithm.MCTS)
        else: 
            print("Error! Read README.md for more details!")
    else:
        main(level="01", algorithm=Algorithm.BFS)