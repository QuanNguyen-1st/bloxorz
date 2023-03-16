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
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
game = Map("level/28.txt")
display = Display(title='Bloxorz Game', map_size=(game.height, game.width))

split1 = 1
split2 = 0

def switchSplit():
    global split1
    global split2
    temp = split1
    split1 = split2
    split2 = temp

def moveGame(i):
    global player
    if game.isPlayerSplitted:
        player = DetachedPlayer(player.p1.Move(i * split1), player.p2.Move(i * split2))
        temp = DetachedPlayer(player.p2, player.p1)
        if temp.hasAttached():
            game.isPlayerSplitted = False
            player = Player(player.p1, player.p2)
    else:
        player = player.Moves(i)
        game.arr = game.newMapIfButtonPressed(player, game.arr)
        player = game.dupButtonPressed(player)

def draw_player():
    if game.isPlayerSplitted:
        Box.draw_box(position=(player.p1.y, player.p1.x), size=(1,1,1))
        Box.draw_box(position=(player.p2.y, player.p2.x), size=(1,1,1))
    else:
        if player.isStanding():
            size = (1,1,2)
        elif player.isHorizontal():
            size = (2,1,1)
        else:
            size = (1,2,1)
        Box.draw_box(position=(player.p2.y, player.p2.x), size=size)

def draw_maps():
    for x in range(game.height):
        for y in range(game.width):
            if x == game.goal.x and y == game.goal.y:
                continue
            elif game.weakArr[x][y]:
                Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['orange'])
            elif game.specialArr[x][y] == 3:
                Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['green'])
            elif game.specialArr[x][y] == 4:
                Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['white'])
            elif game.specialArr[x][y] == 5:
                Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['blue'])
            elif game.specialArr[x][y] == 6:
                Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['pink'])
            elif game.specialArr[x][y] == 7:
                Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['red'])
            elif game.specialArr[x][y] == 8:
                Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['yellow'])
            elif game.arr[x][y]:
                Box.draw_box(position=(y, x), size=(1, 1, -0.3), face_color=colors['gray'])


start_time = time.time()

bfs = BFS(game)
bfs.solve()

print("Time process: ", time.time() - start_time)
winPath = bfs.winPath
print(winPath)
solution = list(winPath.split(" "))
i=0
steps = solution.__len__()

# astar = AStar(game)
# astar.solve()
# print(astar.winPath)

player = Player(Position(game.start.x, game.start.y), Position(game.start.x, game.start.y))
game.isPlayerSplitted = False

Box.draw_box(position=(player.p1.y, player.p1.x), size=(1,1,2))
draw_maps()
display.update()
time.sleep(2)

prev_split = 1

runningAuto = True
while runningAuto:
    draw_player()
    draw_maps()
    display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningAuto = False

    if i >= steps:
        continue

    if solution[i][1] == ',':
        if prev_split == 1:
            switchSplit()
            prev_split = 2
    if solution[i][-2] == ',':
        if prev_split == 2:
            switchSplit()
            prev_split = 1

    if "Right" in solution[i]:
        moveGame(2)
        time.sleep(1)
    elif "Left" in solution[i]:
        moveGame(1)
        time.sleep(1)
    elif "Down" in solution[i]:
        moveGame(4)
        time.sleep(1)
    elif "Up" in solution[i]:
        moveGame(3)
        time.sleep(1)
    i += 1


# runningPlay = True
# while runningPlay:
#     draw_player()
#     draw_maps()
#     display.update()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             runningPlay = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 moveGame(1)
#             if event.key == pygame.K_RIGHT:
#                 moveGame(2)
#             if event.key == pygame.K_UP:
#                 moveGame(3)
#             if event.key == pygame.K_DOWN:
#                 moveGame(4)
#             if event.key == pygame.K_SPACE:
#                 switchSplit()
    
#     if game.canHold(player, game.arr) == False:
#         runningPlay = False


# print(player.p1.x, player.p1.y, player.p2.x, player.p2.y)
