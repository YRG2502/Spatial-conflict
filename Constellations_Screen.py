import pygame

class Constellations_Screen:
    def __init__(self, game):
        self.game = game
        self.background_image = pygame.image.load("constellations_background.jpg")

    def handle_events(self, event):
        # Handle user input specific to this screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check for clicks on constellation images
            # (implement logic to check for clicks on specific constellations)
            pass

    def update(self):
        # Update screen logic here
        pass

    def draw(self):
        # Draw background image and constellation images
        self.game.get_screen().fill((0, 0, 0))
        self.game.get_screen().blit(self.background_image, (0, 0))
