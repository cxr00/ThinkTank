import pygame

import cxr.math.base64

pygame.init()

FPS = 30
TICK = pygame.event.custom_type()
ACCUMULATE = pygame.event.custom_type()
cxr.math.base64.default_base = 7
cxr.math.base64.round_to = 6

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)
