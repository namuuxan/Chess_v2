import os
import pygame
from theme import Theme
from sound import Sound

class Config:
    def __init__(self):
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(os.path.join('assets/sounds/move.wav'))
        self.capture_sound = Sound(os.path.join('assets/sounds/capture.wav'))

    def change_theme(self):
        self.idx += 1
        self.idx %= len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        green = Theme(
            light_bg=(234, 235, 200), dark_bg=(119, 154, 88),
            light_trace=(244, 247, 116), dark_trace=(172, 195, 51),
            light_moves='#C86464', dark_moves='#C84646',
            text_color=(0, 0, 0)
        )
        brown = Theme(
            light_bg=(235, 209, 166), dark_bg=(165, 117, 80),
            light_trace=(245, 234, 100), dark_trace=(209, 185, 59),
            light_moves='#C86464', dark_moves='#C84646',
            text_color=(0, 0, 0)
        )
        blue = Theme(
            light_bg=(229, 228, 200), dark_bg=(60, 95, 135),
            light_trace=(123, 187, 227), dark_trace=(43, 119, 191),
            light_moves='#C86464', dark_moves='#C84646',
            text_color=(255, 255, 255)
        )
        gray = Theme(
            light_bg=(120, 119, 118), dark_bg=(86, 85, 84),
            light_trace=(99, 126, 143), dark_trace=(82, 108, 128),
            light_moves='#C86464', dark_moves='#C84646',
            text_color=(255, 255, 255)
        )

        self.themes = [green, brown, blue, gray]
