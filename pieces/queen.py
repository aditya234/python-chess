from pieces.piece import Piece


class Queen(Piece):
    allilance = None
    position = None

    def __init__(self, alliance, position):
        self.allilance = alliance
        self.position = position

    def tostring(self):
        return "Q" if self.allilance == "Black" else "q"
