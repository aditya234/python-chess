class Tile:
    piece_on_tile = None
    tile_coordinate = None

    def __init__(self, piece_on_tile, tile_coordinate):
        self.piece_on_tile = piece_on_tile
        self.tile_coordinate = tile_coordinate
