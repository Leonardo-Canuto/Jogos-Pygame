class Settings():
    """Uma classe para amazenar todas as configurações da
    insao alienigena."""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        #configuração da tela
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #configurações da espaçonave
        self.ship_speed_factor = 1.5

        # Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_alowed = 3