import json
from atr.moves import Move

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def isValidIndex(self):
        return self.x >= 0 and self.y >= 0
    
    def dx(self, x):
        return Position(self.x + x, self.y)
    
    def dy(self, y):
        return Position(self.x, self.y + y)
    
    def Left(self):
        return self.dy(-1)
    
    def Right(self):
        return self.dy(1)
    
    def Up(self):
        return self.dx(-1)
    
    def Down(self):
        return self.dx(1)
    
    def Move(self, dir: Move):
        if dir == 1:
            return self.Left()
        elif dir == 2:
            return self.Right()
        elif dir == 3:
            return self.Up()
        elif dir == 4:
            return self.Down()
        

    def move(self, dx, dy):
        return Position(self.x + dx, self.y + dy)
    
    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y
    
    def __str__(self):
        return json.dumps([self.x, self.y])