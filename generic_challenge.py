# Import the pygame module used to create graphical apps
import pygame
from random import choice, randint

# Actividad:
# Implementar la siguiente mejora:
# Si el jugador colisiona con bonus_1 recibe 10 puntos
#                             bonus_2 recibe 20 puntos
#                             bonus_3 recibe 30 puntos
# # Module initialization
pygame.init()
# Create a window of a given size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Name your window
pygame.display.set_caption('First game')

POINTS_FONT = pygame.font.SysFont("verdana", 20)

# Create a clock to monitor fps
clock = pygame.time.Clock()

bonus_images = [
    'img/bonus_1.png',
    'img/bonus_2.png',
    'img/bonus_3.png'
]

FRAMES_PER_SECOND = 60
frames_cnt = 0


def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()

    transparent_color = (0, 0, 0)
    surface.set_colorkey(transparent_color)

    # Position of an object to display is held in rect
    rect = surface.get_rect(center=position)

    return [image, surface, rect]


def print_image(img_list) -> None:
    # [image, surface, rect]
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass


def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]


def calculate_player_movement(keys):
    # Player movement
    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_UP]:
        delta_y -= speed
    if keys[pygame.K_DOWN]:
        delta_y += speed
    if keys[pygame.K_RIGHT]:
        delta_x += speed
    if keys[pygame.K_LEFT]:
        delta_x -= speed

    return [delta_x, delta_y]


def limit_position(position):
    x, y = position
    x = max(0, min(x, SCREEN_WIDTH))
    y = max(0, min(y, SCREEN_HEIGHT))
    return [x, y]


def generate_bonus_object():
    # Selecting a random file name to load
    image_name = choice(bonus_images)
    # Selecting random coordinates for a new object
    x = randint(0, SCREEN_WIDTH)
    y = randint(0, SCREEN_HEIGHT)
    # Position variable is a two-element list
    position = [x, y]
    # Create new graphics object using the load_image function
    new_obj = load_image(image_name, position)
    # Add new object to list of all objects
    bonus_objects.append(new_obj)
    pass


def print_bonus_objects():
    # Iterate over bonus objects
    for obj in bonus_objects:
        # Display the object on the screen,
        # using the print_image function
        print_image(obj)
        pass
    pass


def check_collisions():
    global player_points
    rect_player = player[2]

    # You can choose the way to get an index
    # for i in range(len(bonus_objects)):
    #    index = len(bonus_objects) - 1 - i

    for index in range(len(bonus_objects) - 1, -1, -1):
        obj = bonus_objects[index]
        rect = obj[2]
        if rect.colliderect(rect_player):
            bonus_objects.pop(index)
            player_points += 1
            print(f"\rPoints: {player_points}", end='')
            pass
        pass
    pass

def print_points(points: int) -> None:
    text = f"Points: {points}"
    color = [255, 255, 255]
    position = [0, 0]
    label = POINTS_FONT.render(text, False, color)
    screen_surface.blit(label, position)
    pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image('img/player.png', player_pos)
background_color = [9, 42, 121]
# List of bonus objects
# Object is a 3-element list returned by load_image function
bonus_objects = []

# Number of points gathered by player
player_points = 0

# Game loop
# Variable used to decide if window should be closed
game_status = True
# Code running until the app is running
while game_status:

    # Read events registered by the computer
    events = pygame.event.get()

    for event in events:
        # X button pressed - quit the app
        if event.type == pygame.QUIT:
            game_status = False
            # Si se pulsa la tecla [Esc] se sale del programa.
        pass  # for event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                game_status = False
        pass  # for event

    pressed_keys = pygame.key.get_pressed()

    delta_x, delta_y = calculate_player_movement(pressed_keys)

    # Change coordinates values
    player_pos[0] += delta_x
    player_pos[1] += delta_y
    # Check player position limits
    player_pos = limit_position(player_pos)

    # Change the coordinates of an image
    player = set_position_image(player, player_pos)

    # Fill the background
    screen_surface.fill(background_color)
    # Display the player
    print_image(player)

    # Add bonus objects, first do it without the limiting condition ;)
    if frames_cnt % (FRAMES_PER_SECOND * 1) == 0:
        generate_bonus_object()
        pass

    check_collisions()

    print_bonus_objects()

    print_points(player_points)
    
    # Refresh the window
    pygame.display.update()

    frames_cnt += 1

    clock.tick(FRAMES_PER_SECOND)
    pass

print("Application closing")
# Closing the app
pygame.quit()
# Closing script
quit()

