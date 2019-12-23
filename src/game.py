import pygame
import colors
import config
from snake import Snake, Direction
from _thread import *
from item import ItemsManager
from label import Label
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.is_over = False
        self.game_display = pygame.Surface(config.WINDOW_SIZE)
        self.cells = []
        self.snake = Snake(config.SNAKE_START_RECT, 6)
        self.items_manager = ItemsManager(1)

        self.clock = pygame.time.Clock()
        self.score_label = Label("0", "Consolas", 30, colors.WHITE)

    def update_scene(self):
        self.game_display = pygame.display.set_mode(config.WINDOW_SIZE)
        while not self.is_over:
            self.game_display.fill(colors.BACKGROUND_COLOR)

            if self.snake.rect.colliderect(self.items_manager.item.rect):
                self.snake.score += 1
                self.score_label.set_text(str(self.snake.score))
                self.items_manager.append_item()
                #for i in range(3):
                #self.snake.snake_body.insert(0, list([self.snake.rect.x, self.snake.rect.y]))
            else:
                self.snake.snake_body.pop()

            for snake_pos in self.snake.snake_body[1:]:
                if self.snake.snake_body[0] == snake_pos:
                    print("test")
                    sys.exit(-1)


            pygame.draw.rect(self.game_display, self.items_manager.item.color, self.items_manager.item.rect)

            self.snake.update(config.WINDOW_SIZE)
            for tail in self.snake.snake_body:
                pygame.draw.rect(self.game_display, colors.WHITE, pygame.Rect(tail[0], tail[1], 15, 15))

            self.game_display.blit(self.score_label.text_obj, [0, 0])

            self.event_handler()
            pygame.display.flip()
            self.clock.tick(60)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Close!")
                self.is_over = True
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction(Direction.UP)
                if event.key == pygame.K_RIGHT:
                    self.snake.set_direction(Direction.RIGHT)
                if event.key == pygame.K_DOWN:
                    self.snake.set_direction(Direction.DOWN)
                if event.key == pygame.K_LEFT:
                    self.snake.set_direction(Direction.LEFT)
