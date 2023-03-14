from atr.player import Player
from atr.player import DetachedPlayer
from atr.position import Position
from atr.moves import Move
from atr.tiles import Tiles
import atr.button as bt
import copy

class Map:
    arr = None
    weakArr = None
    specialArr = None
    start = None
    goal = None
    width = 0
    height = 0
    buttons = []
    # tile = Tiles()

    def __init__(self, dict):
        self.readLevel(dict)

    def readLevel(self, dict):
        self.arr = []
        with open(dict, 'r') as file:
            self.height, self.width, x, y = [int(a) for a in file.readline().split(' ')]
            self.start = Position(x, y)
            self.weakArr = [[False]*self.width for i in range (self.height)]
            self.specialArr = [[0]*self.width for i in range (self.height)]
            for x in range(self.height):
                row = []
                for (y, val) in enumerate([int(a) for a in file.readline().split(' ')]):
                    if val == 0:
                        row.append(False)
                    else:
                        row.append(True)
                        if val == 9:
                            self.goal = Position(x, y)
                        elif val == 2:
                            self.weakArr[x][y] = True
                        elif val != 1:
                            self.specialArr[x][y] = val
                self.arr.append(row)
            for line in file:
                self.checkSquare([int(a) for a in line.split(' ')])
                    
    def checkSquare(self, num: list):
        x, y = num[0], num[1]
        val = self.specialArr[x][y]
        if val == 3:
            button = Tiles().isNumberThree(num)
            self.buttons.append(button)
        elif val == 4:
            button = Tiles().isNumberFour(num)
            self.buttons.append(button)
        elif val == 5:
            button = Tiles().isNumberFive(num)
            self.buttons.append(button)
        elif val == 6:
            button = Tiles().isNumberSix(num)
            self.buttons.append(button)
        elif val == 7:
            button = Tiles().isNumberSeven(num)
            self.buttons.append(button)
        elif val == 8:
            button = Tiles().isNumberEight(num)
            self.buttons.append(button)

    def hasWon(self, player: Player):
        return player.isStanding() and player.p1.x == self.goal.x and player.p1.y == self.goal.y
    
    def cannotHoldWeak(self, player: Player) -> bool:    
        return self.weakArr[player.p1.x][player.p1.y] and self.weakArr[player.p2.x][player.p2.y] and player.isStanding()
    
    def canHold(self, player: Player, arr: list) -> bool:
        try:
            ans = not self.cannotHoldWeak(player) and \
                arr[player.p1.x][player.p1.y] and \
                arr[player.p2.x][player.p2.y] and \
                player.isValidIndex()
        except IndexError:
            ans = False
        return ans
    
    def newMapIfButtonPressed(self, player: Player, arr: list) -> list:
        newArr = copy.deepcopy(arr)
        for button in self.buttons:
            if (isinstance(button, bt.ButtonX) or isinstance(button, bt.ButtonO)) and button.isPressed(player):
                for pos in button.toggle:
                    newArr[pos[0]][pos[1]] = not newArr[pos[0]][pos[1]]
                for pos in button.close:
                    newArr[pos[0]][pos[1]] = False
                for pos in button.open:
                    newArr[pos[0]][pos[1]] = True
        return newArr
    
    def dupButtonPressed(self, player: Player) -> Player:
        for button in self.buttons:
            if isinstance(button, bt.Dup) and button.isPressed(player):
                return DetachedPlayer(Position(button.location[0][0], button.location[0][1]), \
                                      Position(button.location[1][0], button.location[1][1]))
        return player
    
    def allMoves(self, player: Player, arr: list) -> list:
        moves = []
        if isinstance(player, DetachedPlayer):
            for i in range(1,5):
                newMove1 = DetachedPlayer(player.p1.Move(i), player.p2)
                newMove2 = DetachedPlayer(player.p1, player.p2.Move(i))
                if newMove1.hasAttached():
                    newMove1 = Player(newMove1.p1, newMove1.p2)
                if newMove2.hasAttached():
                    newMove2 = Player(newMove2.p1, newMove2.p2)
                moves.append((newMove1, "(" + str(Move(i)) + ",)", self.newMapIfButtonPressed(newMove1, arr)))
                moves.append((newMove2, "(," + str(Move(i)) + ")", self.newMapIfButtonPressed(newMove2, arr)))
            return moves
        else:
            for i in range(1,5):
                newMove = self.dupButtonPressed(player.Moves(i))
                moves.append((newMove, str(Move(i)), self.newMapIfButtonPressed(newMove, arr)))
            return moves

    def legalMoves(self, player: Player, arr: list) -> list:
        # moves = []
        # if isinstance(player, DetachedPlayer):
        #     for i in range(1,5):
        #         newMove1 = DetachedPlayer(player.p1.Move(i), player.p2)
        #         newMove2 = DetachedPlayer(player.p1, player.p2.Move(i))
        #         if newMove1.hasAttached():
        #             newMove1 = Player(newMove1.p1, newMove1.p2)
        #         if newMove2.hasAttached():
        #             newMove2 = Player(newMove2.p1, newMove2.p2)
        #         moves.append((newMove1, "(" + str(Move(i)) + ",)", self.newMapIfButtonPressed(newMove1, arr)))
        #         moves.append((newMove2, "(," + str(Move(i)) + ")", self.newMapIfButtonPressed(newMove2, arr)))
        #     return [(move, dir, newMap) for (move, dir, newMap) in moves if self.canHold(move, arr)]
        # else:
        #     for i in range(1,5):
        #         newMove = self.dupButtonPressed(player.Moves(i))
        #         moves.append((newMove, str(Move(i)), self.newMapIfButtonPressed(newMove, arr)))
        #     return [(move, dir, newMap) for (move, dir, newMap) in moves if self.canHold(move, arr)]
        return [(move, dir, newMap) for (move, dir, newMap) in self.allMoves(player, arr) if self.canHold(move, arr)]