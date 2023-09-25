import pygame 
from components import *

from ecs.system import System
from ecs.ecs import ECS


class RectRenderer(System):
    
    def __init__(self, surf):
        self.surf = surf

    def update(self, ecs: ECS) -> None:
        for pos, size, color in ecs.get_components([Position, Size, Color]):
            pygame.draw.rect(self.surf, color, (pos.x, pos.y, size.w, size.h), 1)


class Movement(System):

    def update(self, ecs: ECS) -> None:
        dt = ecs.get_global('delta')
        for pos, vel in ecs.get_components([Position, Velocity]):
            pos.x += vel.x * dt
            pos.y += vel.y * dt