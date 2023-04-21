# File created by: Thomas Trombatore


# import libs
import pygame as pg
import os
# import settings 
from settings import *
from sprites import *
# from pg.sprite import Sprite

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# create game class in order to pass properties to the sprites file

class Game:
    def __init__(self):
        # init game window etc.
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("my game")
        self.clock = pg.time.Clock()
        self.running = True
        print(self.screen)
    def new(self):
        # starting a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.player = Player(self)
        # adds platforms to the game and determines if they bounce your player, or disapear etc.
        self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        # self.plat1 = Platform(WIDTH, 50, 0, HEIGHT-50, (150,150,150), "normal")
        self.plat2 = Platform(WIDTH, 60, 0, HEIGHT-40, (255,50,50), "bouncy")
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)
        self.platforms.add(self.plat2)
        
        # adds your player into the game
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
            # determines the range
        for i in range(0,10):
            m = Mob(20,20,(0,255,0))
            # adds mobs to your game
            self.all_sprites.add(m)
            self.enemies.add(m)
        self.run()
    def run(self):
        self.playing = True
        # when playing the timer goes down
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pg.event.get():
            # gives the games boundaries of when to reset or keep playing
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                # gives controls for the player to move around
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            # determines what your platform does. 
            if hits:
                if hits[0].variant == "disappearing":
                    hits[0].kill()
                    self.player.image.fill(0,250,0)
                elif hits[0].variant == "bouncey":
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = -PLAYER_JUMP
                    # changes the color of player when jumping
                    self.player.image.fill(RED)
                else:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    # changes your player to white whenever it lands
                    self.player.image.fill(WHITE)
# Determines what the game looks like and fills in with the colors that are defined.
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        # function
        pg.display.flip()
        # defines the name
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
    def get_mouse_now(self):
        x,y = pg.mouse.get_pos()
        return (x,y)

# instantiate the game class
g = Game()

# starts the game loop
while g.running:
    g.new()

# ends the function
pg.quit()