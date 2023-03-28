import sys
from atr.algorithm import Algorithm
from testnogame import Game
import os, psutil

def main(level, algorithm):
    game = Game(level)
    if algorithm == Algorithm.NONE:
        pass
    else:
        if algorithm == Algorithm.BFS:
            game.solve_with_algorithm(Algorithm.BFS)
        elif algorithm == Algorithm.ASTAR:
            game.solve_with_algorithm(Algorithm.ASTAR)
        elif algorithm == Algorithm.MCTS:
            game.solve_with_algorithm(Algorithm.MCTS)


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
        main(level="06", algorithm=Algorithm.MCTS)