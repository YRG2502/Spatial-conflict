import Constellations_Screen
import pygame

class Game:
  def __init__(self, width, height, title):
    # Initialize Pygame and create the window
    pygame.init()
    self.screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    # self.clock = pygame.time.Clock()

  def run(self):
    running = True
    while running:
      # Handle events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      # Update game objects (can be replaced with specific methods)
      self.update()

      # Draw game objects (can be replaced with specific methods)
      self.draw()

      # Update the display
      pygame.display.flip()

  def update(self):
    # Update game logic here (e.g., player movement, enemy AI)
    pass

  def draw(self):
    # Clear the screen and draw game objects here
    self.screen.fill((0, 0, 0))  # Fill with black color
    # Call drawing methods for game objects here
    pygame.display.update()

  def quit(self):
    # Clean up resources
    pygame.quit()

# Example usage
if __name__ == "__main__":
  game = Game(800, 600, "My Pygame Game")
  game.run()
  game.quit()