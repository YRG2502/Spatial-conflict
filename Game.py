from Constellations_Screen import Constellations_Screen
from Screen_Manager import ScreenManager
import pygame

class Game:
    def __init__(self, width, height, title):
        # Initialize Pygame and create the window
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        # Text
        self.title_font = pygame.font.Font(None, 60)
        self.button_font = pygame.font.Font(None, 40)
        self.input_font = pygame.font.Font(None, 32)

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)

        # Initialize screen manager
        self.screen_manager = ScreenManager(self)

    def run(self):
        self.screen_manager.run()

    def quit(self):
        # Clean up resources
        pygame.quit()

    def switch_screen(self, screen_name):
        self.screen_manager.switch(screen_name)

    def get_screen(self):
        return self.screen

    def get_font(self, size):
        return pygame.font.Font(None, size)
    

if __name__ == "__main__":
    game = Game(800, 600, "Space Exploration")
    constellations_screen = Constellations_Screen(game)
    game.screen_manager.add_screen("Constellations", constellations_screen)
    game.switch_screen("Constellations")
    game.run()
    game.quit()