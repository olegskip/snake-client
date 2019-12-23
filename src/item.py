import pygame
import random
from _thread import *
from time import sleep
import colors
import config


class ItemsManager:
    def __init__(self, time):
        self.item = None
        self.time = time
        self.is_stopped = False
        self.append_item()

    def append_item(self):
        random_choice = random.randint(0, 2)
        random_x = random.randint(50, config.WINDOW_SIZE[0] - 50)
        random_y = random.randint(50, config.WINDOW_SIZE[1] - 50)

        if random_choice == 0 or random_choice == 1 or random_choice == 2:
            self.item = EdibleItem(pygame.Rect(random_x, random_y, 15, 15), colors.EDIBLE_ITEM_COLOR)


class Item:
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color


class EdibleItem(Item):
    def __init__(self, rect, color):
        super().__init__(rect, color)
