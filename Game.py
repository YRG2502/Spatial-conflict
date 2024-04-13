from Constellations_Screen import Constellations_Screen
import pygame

class Game:
  def __init__(self, width, height, title):
    # Initialize Pygame and create the window
    pygame.init()
    self.screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    # self.clock = pygame.time.Clock()

    # Text
    self.title_font = pygame.font.Font(None, 60)
    self.button_font = pygame.font.Font(None, 40)
    self.input_font = pygame.font.Font(None, 32)

    # Colours
    self.WHITE = (255, 255, 255)
    self.BLACK = (0, 0, 0)
    self.BLUE = (0, 0, 255)

  def draw_text(self, text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

  def run(self):
    running = True
    while running:
      # Handle events
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.start_button.collidepoint(event.pos):
            # Add user name

            constellsScreen = Constellations_Screen(self) # need to put in user name screen
            constellsScreen.show()
        

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
    self.start_button = pygame.Rect(300, 290, 160, 60)
    pygame.draw.rect(self.screen, self.BLUE, self.start_button)
    self.draw_text('Space Exploration', self.title_font, self.WHITE, self.screen, 200, 200)
    # Call drawing methods for game objects here
    pygame.display.update()

  def quit(self):
    # Clean up resources
    pygame.quit()

# Example usage
if __name__ == "__main__":
  game = Game(800, 600, "Space Exploration")
  game.run()
  game.quit()