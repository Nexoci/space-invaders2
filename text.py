import pygame
import sys

class customtext(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,font_name,font_size,text_color,text):
        super().__init__()
        font_used = pygame.font.SysFont(font_name, font_size)
        self.text(font_used.render(text, True, (0, 0, 0)), (start_x, start_y))

        self.font_named=font_name
        self.text_color = text_color
        self.text=text
        self.font_used = font_used
        self.font_size=font_size