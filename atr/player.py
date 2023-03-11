from atr.position import Position
from atr.moves import Move
import json

class Player:
    def __init__(self, p1: Position, p2: Position):
        if (p1.x >= p2.x and p1.y >= p2.y):
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1

    def isValidIndex(self) -> bool:
        return self.p1.isValidIndex() and self.p2.isValidIndex()

    def isStanding(self) -> bool:
        return self.p1 == self.p2
    
    def isHorizontal(self) -> bool:
        return self.p1.x == self.p2.x and self.p1.y > self.p2.y
    
    # y -1 -2 -2 -1 -1 -1
    def Left(self):
        if (self.isStanding()):
            return self.dy(-1, -2)
        elif (self.isHorizontal()):
            return self.dy(-2, -1)
        else:  
            return self.dy(-1, -1)
    # y 2 1 1 2 1 1
    def Right(self):
        if (self.isStanding()):
            return self.dy(2, 1)
        elif (self.isHorizontal()):
            return self.dy(1, 2)
        else:  
            return self.dy(1, 1)
    
    # x -1 -2 -1 -1 -2 -1
    def Up(self):
        if (self.isStanding()):
            return self.dx(-1, -2)
        elif (self.isHorizontal()):
            return self.dx(-1, -1)
        else:  
            return self.dx(-2, -1)

    # x 2 1 1 1 1 2    
    def Down(self):
        if (self.isStanding()):
            return self.dx(2, 1)
        elif (self.isHorizontal()):
            return self.dx(1, 1)
        else:  
            return self.dx(1, 2)
            
    def Moves(self, direction:Move):
        if direction == 1: 
            return self.Left()
        elif direction == 2:
            return self.Right()
        elif direction == 3:
            return self.Up()
        elif direction == 4:
            return self.Down()
    
    def dx(self, x1, x2):
        return Player(self.p1.dx(x1), self.p2.dx(x2))
    
    def dy(self, y1, y2):
        return Player(self.p1.dy(y1), self.p2.dy(y2))
        
    def __eq__(self, __o: object) -> bool:
        return self.p1 == __o.p1 and self.p2 == __o.p2

    def __str__(self):
        return json.dumps([str(self.p1), str(self.p2)])
    
class DetachedPlayer(Player):
    def __init__(self, p1: Position, p2: Position):
        self.p1 = p1
        self.p2 = p2

    def hasAttached(self) -> bool:
        return self.p1.x == self.p2.x and abs(self.p1.y - self.p2.y) == 1 or \
               self.p1.y == self.p2.y and abs(self.p1.x - self.p2.x) == 1
    
    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o) or self.p2 == __o.p1 and self.p1 == __o.p2
