import pygame
import random
from screen_elements import ScreenElements, Bee, TextElement

class GameScene: 

    def __init__(self):
        self.bg = ScreenElements(
            image="assets/bg.png", 
            axis_x=0, 
            axis_y=0
        )

        self.bg_aux = ScreenElements(
            image="assets/bg.png", 
            axis_x=0, 
            axis_y=-640
        )
        
        self.spider = ScreenElements(
            image="assets/spider1.png", 
            axis_x=random.randrange(0, 300), 
            axis_y=-50
        )

        self.flower = ScreenElements(
            image="assets/flower1.png", 
            axis_x=random.randrange(0, 300), 
            axis_y=-50
        )

        self.bee = Bee(
            image="assets/bee1.png", 
            axis_x=150, 
            axis_y=600
        )

        self.score = TextElement(
            text_screen="0",
            size=60
        )

        self.lifes = TextElement(
            text_screen="3",
            size=40
        )

        self.change_scene = False
    
    def draw(self, window):
        self.bg.drawing(window)
        self.bg_aux.drawing(window)
        self.bee.drawing(window)
        self.spider.drawing(window)
        self.flower.drawing(window)
        self.score.drawing(window, axis_x=160, axis_y=50)
        self.lifes.drawing(window, axis_x=50, axis_y=50)
    def update(self):
        self.move_bg()
        self.spider.animation(image="spider", tick=8, frames=5)
        self.flower.animation(image="flower", tick=8, frames=3)
        self.bee.animation(image="bee", tick=2, frames=5)
        self.move_spiders()
        self.move_flowers()
        self.bee.collision(group=self.spider.group, name="Spider")
        self.bee.collision(group=self.flower.group, name="Flower")
        self.gameover()
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(str(self.bee.life))

    def move_bg(self):
        self.bg.sprite.rect[1] += 5
        self.bg_aux.sprite.rect[1] += 5

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
        
        if self.bg_aux.sprite.rect[1] >= 0:
            self.bg_aux.sprite.rect[1] = -640
    
    def move_spiders(self):
        self.spider.sprite.rect[1] += 15

        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = ScreenElements(
                image="assets/spider1.png", 
                axis_x=random.randrange(0, 300), 
                axis_y=-50
            )
    
    def move_flowers(self):
        self.flower.sprite.rect[1] += 22

        if self.flower.sprite.rect[1] >= 700:
            self.flower.sprite.kill()
            self.flower = ScreenElements(
                image="assets/flower1.png", 
                axis_x=random.randrange(0, 300), 
                axis_y=-50
            )

    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True