from atr.map import Map
from atr.player import Player
from atr.player import DetachedPlayer
from atr.position import Position
from atr.bfs import BFS
from atr.astar import AStar
import atr.button as bt
import pygame
import sys
import os
import time
from drawing.display import Display
from drawing.box import Box
from drawing.color import colors

game = Map("level/01.txt")

start_time = time.time()

# bfs = BFS(game)
# bfs.solve()

# print("Time process: ", time.time() - start_time)
# print(bfs.winPath)

def draw_maps():
    for x in range(10):
        for y in range(6):
            if x == 7 and y == 4:
                continue
            Box.draw_box(position=(x, y), size=(1, 1, -0.3), face_color=colors['gray'])

pygame.init()
display = Display(title='Bloxorz Game', map_size=(6,10))

x=0
y=0
solution = ["Right", "Right", "Down", "Right", "Right", "Right", "Down"]
i=0
steps = solution.__len__()

running = True
while running:
    Box.draw_box(position=(x,y), size=(1, 1, 2))
    draw_maps()
    display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         x -= 1
        #     if event.key == pygame.K_RIGHT:
        #         x += 1
    if i >= steps:
        continue
    elif solution[i] == "Right":
        x += 1
    elif solution[i] == "Left":
        x -= 1
    elif solution[i] == "Down":
        y += 1
    elif solution[i] == "Up":
        y -= 1
    i += 1

    time.sleep(1)


# astar = AStar(game)
# astar.solve()
# print(astar.winPath)
