import pygame
from board.chess_board import Board

pygame.init()
game_display = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Python Chess")
clock = pygame.time.Clock()

chess_board = Board()
chess_board.create_board()
chess_board.print_board()
quit_game = False

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)  # Number of FPS
