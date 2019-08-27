from board.tile import Tile
from pieces.no_piece import NoPiece


class Board:
    game_tiles = {}

    def __init__(self):
        pass

    def create_board(self):
        for tile in range(64):
            self.game_tiles[tile] = Tile(tile_coordinate=tile, piece_on_tile=NoPiece())
            # print(self.game_tiles[tile].piece_on_tile.tostring())

    def print_board(self):
        count = 0

        for tiles in range(64):
            print('|', end=self.game_tiles[tiles].piece_on_tile.tostring())
            count += 1

            if count == 8:
                print("|", end='\n')
                count = 0
