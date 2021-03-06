import pygame


class Game:
    """ The class is responsible for all thr logic of the game window. """
    def __init__(self, win, hero):
        pygame.init()
        pygame.display.set_caption("Zombie Gun")
        self.win = win
        self.run = True
        self.button = False
        self.start_game = False
        self.hero = hero
        self.clock = pygame.time.Clock()
        self.button_start_game = pygame.draw.rect(self.win, (0, 0, 0), (135, 60, 180, 18))
        self.coins = []
        self.shells = []
        self.zombies = []
        self.skeletons = []
        self.money = 0
        self.total_killed = 0

    def get_button_start_game(self):
        if self.hero.death:
            self.button_start_game = pygame.draw.rect(self.win, (0, 0, 0), (135, 60, 180, 18))
        else:
            self.button_start_game = pygame.draw.rect(self.win, (0, 0, 0), (0, 0, 0, 0))

    def get_start_game(self):
        self.start_game = not self.hero.death

    def stop_music(self):
        """ The method stop music. """
        pygame.mixer.music.stop()

    def start_music(self):
        """ The method start music. """
        pygame.mixer.init()
        pygame.mixer.music.load("documents/XXXTentacion - Look at Me (minus).mp3")
        pygame.mixer.music.play(-1)

    def out_of_game(self):
        """ The method out of game """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
