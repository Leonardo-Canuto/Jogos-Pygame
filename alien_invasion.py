import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game ():
    #Inicia o jogo e cria um objeto para a tela

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Cria uma espaçonave, um grupo de projéteis e um grupo de Alienigenas
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #Cria uma frota de Alienigenas
    gf.create_fleet(ai_settings,screen,aliens)

    #Define a cor de fundo
    bg_color = (230,230,230)

    #Inicia o laço principal do jogo
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
