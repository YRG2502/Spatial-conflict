import pygame

class Username_Input:
  def __init__(self, game):
    self.game = game  # Store reference to the main Game class
    self.name = ""
    self.cursor_visible = True
    self.cursor_timer = 0

  def handle_events(self):
    # Handle user input specific to this screen
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        # Check for clicks on constellation images
        # (implement logic to check for clicks on specific constellations)
        pass

  def draw(self):
    # Draw background image and constellation images
    self.game.screen.fill(self.game.BLACK)
    self.game.draw_text('Enter Your Name:', self.game.input_font, self.game.WHITE, self.game.screen, 280, 200)
    
    # Input box
    input_box = pygame.Rect(250, 280, 250, 40)
    pygame.draw.rect(self.game.screen, self.game.WHITE, input_box, 2)

    self.cursor_timer += 1
    if self.cursor_timer >= 500:
      self.cursor_visible = not self.cursor_visible
      self.cursor_timer = 0
    
    if self.cursor_visible:
      self.game.draw_text(self.name + '|', self.game.input_font, self.game.WHITE, self.game.screen, 260, 290)
    else: 
      self.game.draw_text(self.name, self.game.input_font, self.game.WHITE, self.game.screen, 260, 290)

    # Confirm button
    confirm_button = pygame.Rect(280, 400, 195, 50)
    pygame.draw.rect(self.game.screen, self.game.BLUE, confirm_button)
    self.game.draw_text('Confirm', self.game.button_font, self.game.WHITE, self.game.screen, 320, 410)

    # Back button
    back_button = pygame.Rect(50, 500, 100, 50)
    pygame.draw.rect(self.game.screen, self.game.BLUE, back_button)
    self.game.draw_text('Back', self.game.button_font, self.game.WHITE, self.game.screen, 60, 515)
        
    pygame.display.update()

  def show(self):
    # Display the Constellations Screen
    self.handle_events()
    self.draw()


def __init__ ():
    const = Username_Input()
    const.show()