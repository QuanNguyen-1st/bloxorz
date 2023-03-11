import enum

class Move(enum.Enum):
    Left = 1
    Right = 2
    Up = 3
    Down = 4

    def __str__(self) -> str:
        return str(self.name)
