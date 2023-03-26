import sys
from atr.algorithm import Algorithm
from game import Game
import os, psutil

def main(level, algorithm):
    game = Game(level)
    if algorithm == Algorithm.NONE:
        game.setup()
        game.runningPlay()
    else:
        if algorithm == Algorithm.BFS:
            game.solve_with_algorithm(Algorithm.BFS)
            game.setup()
            game.runningAI()
        elif algorithm == Algorithm.ASTAR:
            game.solve_with_algorithm(Algorithm.ASTAR)
            game.setup()
            game.runningAI()
        elif algorithm == Algorithm.MCTS:
            game.solve_with_algorithm(Algorithm.MCTS)
            game.setup()
            game.runningAI()


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