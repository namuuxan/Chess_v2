import pygame
import sys
from const import *
from game import Game
from menu import Menu
from dragger import Dragger
from square import Square
from move import Move

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.menu = Menu(self.screen)
        self.game = None
        self.hover_row = 0
        self.hover_col = 0

    def start_game(self, mode):
        self.game = Game()
        if mode == 'pvp':
            self.game.gamemode = 'pvp'
        elif mode == 'ai':
            self.game.gamemode = 'ai'

    def mainloop(self):
        clock = pygame.time.Clock()

        while True:
            if self.game:
                self.handle_game_events()
                if self.game:
                    self.game.show_bg(self.screen)
                    self.game.show_pieces(self.screen)
                    self.game.show_hover(self.screen)
                    pygame.display.update()
                    clock.tick(60)

                    if self.game.check_game_over():
                        self.game.display_winner(self.screen)
                        self.game.wait_for_enter()
                        self.game = None
                        self.menu.run()  

            else:
                mode = self.menu.run()
                if mode is not None:
                    if mode == 2:
                        pygame.quit()
                        sys.exit()
                    self.game = None
                    self.start_game('ai' if mode == 0 else 'pvp')

    def handle_game_events(self):
        if not self.game:
            return  

        game = self.game
        dragger = game.dragger

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                dragger.update_mouse(event.pos)
                pos = event.pos
                clicked_row = dragger.mouseY // SQSIZE
                clicked_col = dragger.mouseX // SQSIZE

                if game.board.squares[clicked_row][clicked_col].has_piece():
                    piece = game.board.squares[clicked_row][clicked_col].piece
                    if piece.color == game.next_player:
                        game.select_piece(piece)
                        game.board.calc_moves(piece, clicked_row, clicked_col)
                        dragger.drag_piece(piece)
                        dragger.save_initial(pos)
                        game.show_bg(self.screen)
                        game.show_pieces(self.screen)

            elif event.type == pygame.MOUSEBUTTONUP:
                if dragger.dragging:
                    dragger.update_mouse(event.pos)
                    released_row = dragger.mouseY // SQSIZE
                    released_col = dragger.mouseX // SQSIZE

                    initial = Square(dragger.initial_row, dragger.initial_col)
                    final = Square(released_row, released_col)
                    move = Move(initial, final)

                    if game.board.valid_move(dragger.piece, move):
                        captured = game.board.squares[released_row][released_col].has_piece()
                        game.board.move(dragger.piece, move)
                        game.sound_effect(captured)
                        game.show_bg(self.screen)
                        game.show_pieces(self.screen)
                        game.next_turn()

                        if game.gamemode == 'ai':
                            game.unselect_piece()
                            game.show_pieces(self.screen)
                            pygame.display.update()
                            move = game.ai.eval(game.board)
                            initial = move.initial
                            final = move.final
                            piece = game.board.squares[initial.row][initial.col].piece
                            captured = game.board.squares[final.row][final.col].has_piece()
                            game.board.move(piece, move)
                            game.sound_effect(captured)
                            game.show_bg(self.screen)
                            game.show_pieces(self.screen)
                            game.next_turn()

                game.unselect_piece()
                dragger.undrag_piece()

            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                self.hover_row = pos[1] // SQSIZE
                self.hover_col = pos[0] // SQSIZE
                game.set_hover(self.hover_row, self.hover_col)

                if dragger.dragging:
                    dragger.update_mouse(event.pos)
                    game.show_bg(self.screen)
                    game.show_pieces(self.screen)
                    game.show_hover(self.screen)
                    dragger.update_blit(self.screen)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game = None
                    self.menu.run()  
                elif event.key == pygame.K_RETURN and game.winner:
                    self.game = None
                    self.menu.run()  
                elif event.key == pygame.K_a:
                    game.change_gamemode()
                elif event.key == pygame.K_3:
                    game.ai.depth = 3
                elif event.key == pygame.K_4:
                    game.ai.depth = 4
                elif event.key == pygame.K_t:
                    game.change_theme()
                elif event.key == pygame.K_r:
                    pass

if __name__ == '__main__':
    m = Main()
    m.mainloop()
