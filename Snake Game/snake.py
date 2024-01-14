import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake and food properties
snake_block = 20
snake_speed = 15

clock = pygame.time.Clock()
food_count = 1

# Function to draw checkerboard background
def draw_background(surface):
    tile_color_1 = (170, 215, 81)
    tile_color_2 = (162, 209, 73)
    tile_size = 40
    for y in range(0, int(height / tile_size)):
        for x in range(0, int(width / tile_size)):
            r = pygame.Rect((x * tile_size, y * tile_size), (tile_size, tile_size))
            pygame.draw.rect(surface, tile_color_1 if (x + y) % 2 == 0 else tile_color_2, r)

# Function to draw the snake
def draw_snake_block(surface, position):
    block_inner = (position[0] + 2, position[1] + 2, snake_block - 4, snake_block - 4)
    pygame.draw.rect(surface, black, position)
    pygame.draw.rect(surface, (0, 100, 0), block_inner)

# Function to draw the food
def draw_food(surface, position):
    pygame.draw.circle(surface, red, (int(position[0] + snake_block / 2), int(position[1] + snake_block / 2)), snake_block // 2)

# Function to display the score
def your_score(score):
    font = pygame.font.SysFont('Arial', 35)
    text = font.render('Score: ' + str(score), True, black)
    game_display.blit(text, [0, 0])

# Function to draw the border
def draw_border(surface, thickness):
    pygame.draw.rect(surface, black, [0, 0, width, thickness])  # Top border
    pygame.draw.rect(surface, black, [0, 0, thickness, height])  # Left border
    pygame.draw.rect(surface, black, [0, height - thickness, width, thickness])  # Bottom border
    pygame.draw.rect(surface, black, [width - thickness, 0, thickness, height])  # Right border

def set_snake_speed():
    global snake_speed
    speed_set = False
    while not speed_set:
        game_display.fill((50, 50, 50))  # Dark background
        font = pygame.font.SysFont('Comic Sans MS', 20)
        instruction_text = font.render('Enter Snake Speed (1-20) and press Enter:', True, (200, 200, 200))
        value_text = font.render(str(snake_speed), True, (0, 255, 255))
        game_display.blit(instruction_text, [width / 4, height / 3])
        game_display.blit(value_text, [width / 2, height / 2])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and snake_speed > 0:
                    speed_set = True
                elif event.key >= pygame.K_1 and event.key <= pygame.K_9:
                    snake_speed = int(chr(event.key))
                elif event.key == pygame.K_0 and snake_speed > 1:
                    snake_speed = 10  # Assuming 10 is the max speed


# Menu screen function
def game_menu():

    menu = True
    while menu:
        game_display.fill((50, 50, 50))  # Dark background
        font = pygame.font.SysFont('Comic Sans MS', 60)  # Larger, more playful font
        title = font.render('Snake Game', True, (200, 200, 200))
        game_display.blit(title, [width / 2 - title.get_width() / 2, height / 4])

        font = pygame.font.SysFont('Comic Sans MS', 40)
        # Draw a horizontal snake icon
        draw_snake_icon(game_display, [width / 2 - 100, height / 4 - 25], 200)

        start_game_text = font.render('Press S to Start Game', True, (255, 255, 0))
        set_food_text = font.render('Press F to Set Food Quantity', True, (0, 255, 0))
        set_speed_text = font.render('Press P to Set Snake Speed', True, (0, 255, 255))
        game_display.blit(start_game_text, [width / 2 - start_game_text.get_width() / 2, height / 2])
        game_display.blit(set_food_text, [width / 2 - set_food_text.get_width() / 2, height / 2 + 50])
        game_display.blit(set_speed_text, [width / 2 - set_speed_text.get_width() / 2, height / 2 + 100])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    menu = False
                    game_loop()
                elif event.key == pygame.K_f:
                    set_food_quantity()
                elif event.key == pygame.K_p:
                    set_snake_speed()
            elif event.type == pygame.QUIT:
                pygame.quit()
                return




def draw_snake_icon(surface, position, size):
    segments = 8
    segment_size = size // segments
    eye_size = segment_size // 4
    eye_offset_x = segment_size // 3
    eye_offset_y = segment_size // 4
    mouth_width = segment_size // 2
    mouth_height = segment_size // 4

    for i in range(segments):
        segment_center = (position[0] + i * segment_size, position[1])
        pygame.draw.circle(surface, (0, 255, 0), segment_center, segment_size // 2)

        # Drawing the face on the first segment
        if i == segments-1:
            # Eyes
            pygame.draw.circle(surface, (255, 255, 255), (segment_center[0] - eye_offset_x, segment_center[1] - eye_offset_y), eye_size)
            pygame.draw.circle(surface, (255, 255, 255), (segment_center[0] + eye_offset_x, segment_center[1] - eye_offset_y), eye_size)

            # Pupils
            pygame.draw.circle(surface, (0, 0, 0), (segment_center[0] - eye_offset_x, segment_center[1] - eye_offset_y), eye_size // 2)
            pygame.draw.circle(surface, (0, 0, 0), (segment_center[0] + eye_offset_x, segment_center[1] - eye_offset_y), eye_size // 2)

            # Mouth
            mouth_rect = [segment_center[0] - mouth_width // 2, segment_center[1] + eye_offset_y, mouth_width, mouth_height]
            pygame.draw.ellipse(surface, (255, 0, 0), mouth_rect)

# Function to set food quantity
def set_food_quantity():
    global food_count
    quantity_set = False
    while not quantity_set:
        game_display.fill((50, 50, 50))  # Dark background
        font = pygame.font.SysFont('Comic Sans MS', 20)
        instruction_text = font.render('Enter Food Quantity (1-10) and press Enter:', True, (200, 200, 200))
        value_text = font.render(str(food_count), True, (255, 255, 0))
        game_display.blit(instruction_text, [width / 4, height / 3])
        game_display.blit(value_text, [width / 2, height / 2])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and food_count > 0:
                    quantity_set = True
                elif event.key >= pygame.K_1 and event.key <= pygame.K_9:
                    food_count = int(chr(event.key))
            elif event.type == pygame.QUIT:
                pygame.quit()
                return

def your_score(score):
    font = pygame.font.SysFont('Arial', 25)  # Smaller and a commonly used font
    text = font.render('Score: ' + str(score), True, black)
    game_display.blit(text, [width - 150, 10])  # Positioning it at the top right corner

# Function for game over screen
def game_over_screen():
    global length_of_snake
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)  # Semi-transparent overlay
    overlay.fill((0, 0, 0, 180))  # Black with alpha
    game_display.blit(overlay, (0, 0))

    font = pygame.font.SysFont('Comic Sans MS', 40)
    mesg = font.render("You Lost! Q-Quit, C-Play Again, M-Menu", True, (255, 100, 100))
    game_display.blit(mesg, [width / 2 - mesg.get_width() / 2, height / 3])
    your_score(length_of_snake - 1)

# Main game loop
def game_loop():
    global length_of_snake, snake_speed

    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Generate initial positions of the food
    food_positions = []
    for _ in range(food_count):
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        food_positions.append([foodx, foody])

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            game_over_screen()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                    if event.key == pygame.K_m:
                        game_over = False
                        game_close = False
                        game_menu()  # Return to the menu

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        draw_background(game_display)
        draw_border(game_display, 10)

        # Draw the food
        for food_position in food_positions:
            draw_food(game_display, food_position)

        # Draw the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collision with self
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        for block in snake_list:
            draw_snake_block(game_display, [block[0], block[1], snake_block, snake_block])

        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake ate food
        for food_position in food_positions[:]:
            snake_head_center = (x1 + snake_block / 2, y1 + snake_block / 2)
            food_center = (food_position[0] + snake_block / 2, food_position[1] + snake_block / 2)
            distance = ((snake_head_center[0] - food_center[0]) ** 2 + (snake_head_center[1] - food_center[1]) ** 2) ** 0.5

            if distance < snake_block:
                food_positions.remove(food_position)
                length_of_snake += 1
                # Generate new food position
                new_foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                new_foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                food_positions.append([new_foodx, new_foody])

        clock.tick(snake_speed)  # Control the snake speed

    pygame.quit()
    quit()



# Start the game with the menu
game_menu()


