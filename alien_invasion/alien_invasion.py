#!/usr/bin/env python3
import sys
import pygame

from settings import Settings

def run_game():
    #initialise
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #main loop
    while True:
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
