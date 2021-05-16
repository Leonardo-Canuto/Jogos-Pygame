import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        '''inicializa a espaçonave e define sua posição inicial.'''
        self.screen = screen
        self.ai_settings = ai_settings

        #carrega a imagem da espaçonave e obtem seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)

        #Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Atuliza a posição da espaçonave de acordo com a flag de movimento'''
        # Atualiza o centro da espaçonave, e nao o retangulo
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Atualiza o objeto rect de acordo com o self.center
        self.rect.centerx = self.center

    def blitme(self):
        '''DESENHA A ESPAÇONAVE EM SUA POSIÇÃO ATUAL'''
        self.screen.blit(self.image,self.rect)