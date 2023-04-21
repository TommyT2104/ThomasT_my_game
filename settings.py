# File Created by Thomas Trombatore

# determines width and height
WIDTH = 800
HEIGHT = 600
# gives the player movement speeds
PLAYER_ACC = 0
PLAYER_FRICTION = -20
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
# gives the mobs movement speeds
MOB_ACC = 2
MOB_FRICTION = -0.3
# defines the colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
FPS = 60
# when playing the game is running
RUNNING = True
SCORE = 0
# when paused the function is not running
PAUSED = False

# creates the platforms inside the game
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (200,200,200), "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20, (100,255,100), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"),
                 (350, 200, 100, 20, (200,200,200), "normal"),
                 (175, 100, 50, 20, (255,255,255), "normal")
                 (600, HEIGHT - 450, 100, 20, (255,50,50), "bouncy")
                 (165, 151, 65, 10, (0,0,0), "disapearing")]