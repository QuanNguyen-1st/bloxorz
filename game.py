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

game = Map("level/04.txt")

start_time = time.time()

bfs = BFS(game)
bfs.solve()

print("Time process: ", time.time() - start_time)
winPath = bfs.winPath
print(winPath)
solution = list(winPath.split(" "))

# astar = AStar(game)
# astar.solve()
# print(astar.winPath)

def draw_maps():
    for x in range(game.width):
        for y in range(game.height):
            if x == game.goal.y and y == game.goal.x:
                continue
            elif game.weakArr[y][x]:
                Box.draw_box(position=(x, y), size=(1, 1, -0.3), face_color=colors['orange'])
            elif game.arr[y][x]:
                Box.draw_box(position=(x, y), size=(1, 1, -0.3), face_color=colors['gray'])
            

pygame.init()
display = Display(title='Bloxorz Game', map_size=(6,10))

x=game.start.x
y=game.start.y
player = Player(Position(x,y), Position(x,y))
i=0
steps = solution.__len__()

Box.draw_box(position=(player.p1.y, player.p1.x), size=(1,1,2))
draw_maps()
display.update()
time.sleep(2)

runningAuto = False
while runningAuto:

    if player.isStanding():
        size = (1,1,2)
    elif player.isHorizontal():
        size = (2,1,1)
    else:
        size = (1,2,1)
    Box.draw_box(position=(player.p2.y, player.p2.x), size=size)
    draw_maps()
    display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningAuto = False
    if i >= steps:
        continue
    elif solution[i] == "Right":
        player = player.Moves(2)
    elif solution[i] == "Left":
        player = player.Moves(1)
    elif solution[i] == "Down":
        player = player.Moves(4)
    elif solution[i] == "Up":
        player = player.Moves(3)
    i += 1

    time.sleep(1)


runningPlay = True
while runningPlay:
    if player.isStanding():
        size = (1,1,2)
    elif player.isHorizontal():
        size = (2,1,1)
    else:
        size = (1,2,1)
    Box.draw_box(position=(player.p2.y, player.p2.x), size=size)
    draw_maps()
    display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player = player.Moves(1)
            if event.key == pygame.K_RIGHT:
                player = player.Moves(2)
            if event.key == pygame.K_UP:
                player = player.Moves(3)
            if event.key == pygame.K_DOWN:
                player = player.Moves(4)