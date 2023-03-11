from atr.position import Position
from atr.player import Player

class Button:
    def __init__(self, pos: Position) -> None:
        self.pos = pos

class ButtonX(Button):
    def __init__(self, pos: Position, toggle: list, open: list, close: list) -> None:
        super().__init__(pos)
        self.toggle = toggle
        self.open = open
        self.close = close


    def isPressed(self, player: Player):
        return player.isStanding() and player.p1 == self.pos


class ButtonO(Button):
    def __init__(self, pos: Position, toggle: list, open: list, close: list) -> None:
        super().__init__(pos)
        self.toggle = toggle
        self.open = open
        self.close = close
    
    def isPressed(self, player: Player):
        return player.p1 == self.pos or player.p2 == self.pos

class Dup(Button):
    def __init__(self, pos: Position, location: list) -> None:
        super().__init__(pos)
        self.location = location

    def isPressed(self, player: Player):
        return player.isStanding() and player.p1 == self.pos
        