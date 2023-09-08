import pygame
from menu import MenuScene, GameOverScene
from game import GameScene
class MainScreen:
    def __init__(self, sizex, sizey, title):
        pygame.init()
        
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sounds/bg.ogg")
        pygame.mixer.music.play(-1) #-1 music in loop

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = MenuScene(image="assets/start.png")
        self.game = GameScene()
        self.gameover = GameOverScene(image="assets/gameover.png")

        self.loop = True
        self.fps = pygame.time.Clock()
       
    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.bee.move_bee(events)
            else:
                self.gameover.events(events)

    def draw(self):
        if not self.menu.change_scene:            
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()
        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.bee.life = 3
            self.game.bee.pts = 0


    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()