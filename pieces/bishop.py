from pieces.piece import Piece


class Bishop(Piece):
    allilance = None
    position = None

    def __init__(self, alliance, position):
        self.allilance = alliance
        self.position = position


    def tostring(self):
        return "B" if self.allilance == "Black" else "b"
