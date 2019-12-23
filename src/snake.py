from enum import Enum
from time import sleep


class Snake:
    def __init__(self, rect, speed):
        self.rect = rect
        self.direction = Direction.RIGHT
        self.is_control_locked = False
        self.speed = speed
        self.score = 0
        self.snake_body = [[self.rect.x, self.rect.y], [self.rect.x - 15, self.rect.y - 15], [self.rect.x - 30, self.rect.y - 30]]

    is_control_locked = False

    def set_direction(self, direction):
        if not self.is_control_locked:
            if direction == direction.UP and self.direction != Direction.DOWN \
                    or direction == direction.RIGHT and self.direction != Direction.LEFT \
                    or direction == direction.DOWN and self.direction != Direction.UP \
                    or direction == direction.LEFT and self.direction != Direction.RIGHT:
                self.direction = direction
                self.is_control_locked = True

    def control_handler(self, max_pos):
        self.is_control_locked = False
        if self.direction == Direction.UP:
            if self.rect.top >= 0:
                self.rect.y -= self.speed
            else:
                self.rect.y = max_pos[1]

        elif self.direction == Direction.RIGHT:
            if self.rect.right <= max_pos[0]:
                self.rect.x += self.speed
            else:
                self.rect.x = 0

        elif self.direction == Direction.DOWN:
            if self.rect.bottom <= max_pos[1]:
                self.rect.y += self.speed
            else:
                self.rect.y = 0

        elif self.direction == Direction.LEFT:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = max_pos[0]

    def update(self, max_pos):
        self.control_handler(max_pos)

        self.snake_body.insert(0, list([self.rect.x, self.rect.y]))



class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
