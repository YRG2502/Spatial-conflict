import pygame

class Constellations_Screen:
  def __init__(self, game):
    self.game = game  # Store reference to the main Game class
    self.background_image = pygame.image.load("constellations_background.jpg")

  def handle_events(self):
    # Handle user input specific to this screen
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        # Check for clicks on constellation images
        # (implement logic to check for clicks on specific constellations)
        pass

  def draw(self):
    # Draw background image and constellation images
    self.game.screen.blit(self.background_image, (0, 0))
    self.start_button = pygame.Rect(400, 290, 160, 60)
    pygame.draw.rect(self.screen, self.BLUE, self.start_button)
    pygame.display.update()

  def show(self):
    # Display the Constellations Screen
    self.handle_events()
    self.draw()


def __init__ ():
    const = Constellations_Screen()
    const.show()