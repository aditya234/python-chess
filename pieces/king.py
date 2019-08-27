from pieces.piece import Piece


class King(Piece):
    allilance = None
    position = None

    def __init__(self, alliance, position):
        self.allilance = alliance
        self.position = position

    def tostring(self):
        return "K" if self.allilance == "Black" else "k"
