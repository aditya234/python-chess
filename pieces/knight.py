from pieces.piece import Piece


class Knight(Piece):
    allilance = None
    position = None

    def __init__(self, alliance, position):
        self.allilance = alliance
        self.position = position

    def tostring(self):
        return "N" if self.allilance == "Black" else "n"
