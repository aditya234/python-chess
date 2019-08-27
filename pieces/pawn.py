from pieces.piece import Piece


class Pawn(Piece):
    allilance = None
    position = None

    def __init__(self, alliance, position):
        self.allilance = alliance
        self.position = position

    def tostring(self):
        return "P" if self.allilance == "Black" else "p"
