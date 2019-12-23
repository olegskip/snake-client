import pygame


class Label:
    def __init__(self, text, font_name, font_size, font_color, background_color=None):
        self.current_color = font_color
        self.current_background_color = background_color
        self.current_font = pygame.font.SysFont(font_name, font_size)
        self.text_obj = self.current_font.render(text, False, self.current_color, self.current_background_color)

    def set_text(self, text):
        self.text_obj = self.current_font.render(text, False, self.current_color, self.current_background_color)
