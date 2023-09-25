# import pyray as pr
import pygame 
from ecs.ecs import ECS

from components import *
from systems import *

display = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
FPS = 60

ecs = ECS()
player = ecs.create_entity(
    (
        Velocity(50, 0),
        Position(50, 50),
        Size(50, 100),
        Color(0, 0, 0),
    )
)
ecs.add_system(RectRenderer(display), 1)
ecs.add_system(Movement(), 0)

ecs.add_global('delta', 0.0)



while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
    dt = clock.tick(FPS) / 1000
    ecs.update_global('delta', dt)
    
    display.fill((255, 255, 255))
    ecs.update_systems()
    pygame.display.flip()


