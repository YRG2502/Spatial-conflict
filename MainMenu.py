import pygame
import sys

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Exploration')

# Fonts
title_font = pygame.font.Font(None, 60)
button_font = pygame.font.Font(None, 40)
input_font = pygame.font.Font(None, 32)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(BLACK)
        
        draw_text('Space Exploration', title_font, WHITE, screen, 200, 200)
        
        # Start button
        start_button = pygame.Rect(300, 290, 160, 60)
        pygame.draw.rect(screen, BLUE, start_button)
        draw_text('Start', button_font, WHITE, screen, 345, 310)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    player_name = input_screen()
                    if player_name == "BACK":
                        continue  # Return to the main menu
                    # else:
                    #     level_selection(player_name)
        
        pygame.display.update()

def input_screen():
    name = ""
    cursor_visible = True
    cursor_timer = 0

    while True:
        screen.fill(BLACK)
        
        draw_text('Enter Your Name:', input_font, WHITE, screen, 280, 200)
        
        # Input box
        input_box = pygame.Rect(250, 280, 250, 40)
        pygame.draw.rect(screen, WHITE, input_box, 2)
        
        # Draw the text with a flashing cursor
        cursor_timer += 1
        if cursor_timer >= 500:  # Adjust the blinking speed by changing this value
            cursor_visible = not cursor_visible
            cursor_timer = 0
        
        if cursor_visible:
            draw_text(name + '|', input_font, WHITE, screen, 260, 290)
        else:
            draw_text(name, input_font, WHITE, screen, 260, 290)

        # Confirm button
        confirm_button = pygame.Rect(280, 400, 195, 50)
        pygame.draw.rect(screen, BLUE, confirm_button)
        draw_text('Confirm', button_font, WHITE, screen, 320, 410)

        # Back button
        back_button = pygame.Rect(50, 500, 100, 50)
        pygame.draw.rect(screen, BLUE, back_button)
        draw_text('Back', button_font, WHITE, screen, 60, 515)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    return name
                else:
                    name += event.unicode
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    return "BACK"
                elif confirm_button.collidepoint(event.pos):
                    level_selection(name)
                
        pygame.display.update()


def level_selection(name):
    while True:
        screen.fill(BLACK)
        draw_text('Level Selection', title_font, WHITE, screen, 200, 200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    player_name = main_menu()
    print(f'Hello, {player_name}!')
    pygame.quit()
    sys.exit()
