from dataclasses import dataclass
import pygame
# from ecs.component import Component

@dataclass
class Rectangle(object):
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    h: float = 0.0


# @dataclass
class Color(pygame.Color):
    def __init__(self, r, g, b, a=255):
        super().__init__(r, g, b, a)


@dataclass
class Position(object):
    x: float = 0.0
    y: float = 0.0


@dataclass
class Velocity(object):
    x: float = 0.0
    y: float = 0.0


@dataclass
class Size:
    w: float = 0.0
    h: float = 0.0