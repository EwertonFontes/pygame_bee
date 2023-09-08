import pygame
from screen_elements import ScreenElements

class MenuScene:
    image: str
    def __init__(self, image):
        self.bg = ScreenElements(
            image=image, 
            axis_x=0, 
            axis_y=0
        )
        self.change_scene = False

    def draw(self, window):
        self.bg.group.draw(window)
    
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True


class GameOverScene(MenuScene):
    def __init__(self, image):
        super().__init__(image)
    
    