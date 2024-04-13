import pygame

class ScreenManager:
    def __init__(self, game):
        self.game = game
        self.screens = {}
        self.current_screen = None

    def add_screen(self, name, screen):
        self.screens[name] = screen

    def switch(self, screen_name):
        if screen_name in self.screens:
            self.current_screen = self.screens[screen_name]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.current_screen.handle_events(event)

            self.current_screen.update()
            self.current_screen.draw()
            pygame.display.flip()