from atr.map import Map
from atr.player import Player
from atr.player import DetachedPlayer
from atr.position import Position
from atr.bfs import BFS
from atr.astar import AStar
from atr.monte_carlo import MCTS
from atr.algorithm import Algorithm
import atr.button as bt
import pygame
import sys
import os, psutil
import time
from drawing.display import Display
from drawing.box import Box
from drawing.color import colors
from OpenGL.GL import *
from OpenGL.GLU import *

def count_steps(path):
    count = 0
    for step in path:
        if "Up" in step or "Down" in step or "Left" in step or "Right" in step:
            count += 1
    return count

class Game:
    def __init__(self, level):
        temp_str = "level/" + level + ".txt" 
        self.game = Map(temp_str)

    def switchSplit(self):
        temp = self.split1
        self.split1 = self.split2
        self.split2 = temp

    def moveGame(self, i):
        if self.game.isPlayerSplitted:
            self.player = DetachedPlayer(self.player.p1.Move(i * self.split1), self.player.p2.Move(i * self.split2))
            if self.split1 == 1:
                temp_split = DetachedPlayer(self.player.p1, self.game.goal)
            else:
                temp_split = DetachedPlayer(self.player.p2, self.game.goal)
            self.game.arr = self.game.newMapIfButtonPressed(temp_split, self.game.arr)
            temp = DetachedPlayer(self.player.p2, self.player.p1)
            if temp.hasAttached():
                self.game.isPlayerSplitted = False
                self.player = Player(self.player.p1, self.player.p2)
        else:
            self.player = self.player.Moves(i)
            self.game.arr = self.game.newMapIfButtonPressed(self.player, self.game.arr)
            self.player = self.game.dupButtonPressed(self.player)

    def draw_player(self):
        if self.game.isPlayerSplitted:
            Box.draw_box(position=(self.player.p1.y, self.player.p1.x), size=(1,1,1))
            Box.draw_box(position=(self.player.p2.y, self.player.p2.x), size=(1,1,1))
        else:
            if self.player.isStanding():
                size = (1,1,2)
            elif self.player.isHorizontal():
                size = (2,1,1)
            else:
                size = (1,2,1)
            Box.draw_box(position=(self.player.p2.y, self.player.p2.x), size=size)

    def draw_maps(self):
        for x in range(self.game.height):
            for y in range(self.game.width):
                if x == self.game.goal.x and y == self.game.goal.y:
                    continue
                elif self.game.weakArr[x][y]:
                    Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['orange'])
                elif self.game.specialArr[x][y] == 3:
                    Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['green'])
                elif self.game.specialArr[x][y] == 4:
                    Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['white'])
                elif self.game.specialArr[x][y] == 5:
                    Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['blue'])
                elif self.game.specialArr[x][y] == 6:
                    Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['pink'])
                elif self.game.specialArr[x][y] == 7:
                    Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['red'])
                elif self.game.specialArr[x][y] == 8:
                    Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['yellow'])
                elif self.game.arr[x][y]:
                    Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['gray'])

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

        print("Time process: ", time.time() - start_time)
        print("Total node explored:", game_to_solve.VNode_count)
        self.memory = process.memory_info().rss / 1024 / 1024 - temp_memory
        print("Memory used to solve:", self.memory, "MB")

        winPath = game_to_solve.winPath
        self.solution = list(winPath.split(" "))
        self.solution_len = self.solution.__len__()

        if (algorithm == Algorithm.MCTS and game_to_solve.can_find_win_path == False):
            print("Haven't found win path, best path so far is:", winPath)
        else:
            print("Total steps:", count_steps(self.solution))
            print("The detail steps:", winPath)

    def setup(self):
        pygame.init()
        self.display = Display(title='Bloxorz Game', map_size=(self.game.height+1, self.game.width+1))
        self.time_sleep = 0.5
        self.player = Player(Position(self.game.start.x, self.game.start.y), Position(self.game.start.x, self.game.start.y))
        self.prev_split = 1
        self.split1 = 1
        self.split2 = 0
        self.game.isPlayerSplitted = False
        Box.draw_box(position=(self.player.p1.y, self.player.p1.x), size=(1,1,2))
        self.draw_maps()
        self.display.update()
        time.sleep(2)

    def runningAI(self):
        i = 0
        runningAI = True
        while runningAI:
            self.draw_player()
            self.draw_maps()
            self.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runningAI = False

            if i >= self.solution_len:
                continue

            if self.solution[i].__len__() >= 1 and self.solution[i][1] == ',':
                if self.prev_split == 1:
                    self.switchSplit()
                    self.prev_split = 2
            if self.solution[i].__len__() >= 1 and self.solution[i][-2] == ',':
                if self.prev_split == 2:
                    self.switchSplit()
                    self.prev_split = 1

            if "Right" in self.solution[i]:
                self.moveGame(2)
                time.sleep(self.time_sleep)
            elif "Left" in self.solution[i]:
                self.moveGame(1)
                time.sleep(self.time_sleep)
            elif "Down" in self.solution[i]:
                self.moveGame(4)
                time.sleep(self.time_sleep)
            elif "Up" in self.solution[i]:
                self.moveGame(3)
                time.sleep(self.time_sleep)
            i += 1

    def runningPlay(self):
        runningPlay = True
        while runningPlay:
            self.draw_player()
            self.draw_maps()
            self.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runningPlay = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.moveGame(1)
                    if event.key == pygame.K_RIGHT:
                        self.moveGame(2)
                    if event.key == pygame.K_UP:
                        self.moveGame(3)
                    if event.key == pygame.K_DOWN:
                        self.moveGame(4)
                    if event.key == pygame.K_SPACE:
                        self.switchSplit()
            
            if self.game.canHold(self.player, self.game.arr) == False:
                runningPlay = False

