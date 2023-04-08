class Position:
    width = None
    height = None
    top = None
    left = None

    def __init__(self, width: int, height: int, top: int, left: int):
        self.width = width
        self.height = height
        self.left = left
        self.top = top
