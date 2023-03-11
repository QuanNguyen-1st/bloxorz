import enum
import atr.button as bt
from atr.position import Position

class Tiles:
    # Nothing = 0
    # Normal = 1
    # Weak = 2
    # X_open_close = 3
    # O_close = 4
    # O_open_close = 5
    # O_open = 6
    # Dup = 7
    # X_open = 8
    # Goal = 9
    def isNumberThree(self, arr: list) -> bt.ButtonX:
        x, y = arr[0], arr[1]
        toggle = []
        open = []
        close = []
        numToggle = arr[2]
        index = 2
        for i in range (numToggle):
            toggle.append([arr[2*i + 3], arr[2*i + 4]])
        index = index + 1 + 2*numToggle
        if index < len(arr):
            numClose = arr[index]
            for i in range (numClose):
                close.append([arr[index + 2*i + 1], arr[index+2*i+2]])
            index = index + 1 + 2*numClose
        if index < len(arr):
            numOpen = arr[index]
            for i in range (numOpen):
                open.append([arr[index + 2*i + 1], arr[index+2*i+2]])
        return bt.ButtonX(Position(x, y), toggle, open, close)
    
    def isNumberFour(self, arr: list) -> bt.ButtonO:
        x, y = arr[0], arr[1]
        close = []
        num = arr[2]
        for i in range (num):
            close.append([arr[2*i + 3],arr[2*i + 4]])
        return bt.ButtonO(Position(x, y), [], [], close)
    
    def isNumberFive(self, arr: list) -> bt.ButtonO:
        x, y = arr[0], arr[1]
        toggle = []
        open = []
        close = []
        numToggle = arr[2]
        index = 2
        for i in range (numToggle):
            toggle.append([arr[2*i + 3], arr[2*i + 4]])
        index = index + 1 + 2*numToggle
        if index < len(arr):
            numClose = arr[index]
            for i in range (numClose):
                close.append([arr[index + 2*i + 1], arr[index+2*i+2]])
            index = index + 1 + 2*numClose
        if index < len(arr):
            numOpen = arr[index]
            for i in range (numOpen):
                open.append([arr[index + 2*i + 1], arr[index+2*i+2]])
        return bt.ButtonO(Position(x, y), toggle, open, close)
    
    def isNumberSix(self, arr: list) -> bt.ButtonO:
        x, y = arr[0], arr[1]
        open = []
        num = arr[2]
        for i in range (num):
            open.append([arr[2*i + 3],arr[2*i + 4]])
        return bt.ButtonO(Position(x, y), [], open, [])
    
    def isNumberSeven(self, arr: list) -> bt.Dup:
        x, y = arr[0], arr[1]
        return bt.Dup(Position(x, y), [[arr[3], arr[4]], [arr[5], arr[6]]])
    
    def isNumberEight(self, arr: list) -> bt.ButtonX:
        x, y = arr[0], arr[1]
        open = []
        num = arr[2]
        for i in range (num):
            open.append([arr[2*i + 3],arr[2*i + 4]])
        return bt.ButtonX(Position(x, y), [], open, [])