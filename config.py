import pygame

# General game settings
GAME_TITLE = "Cruise Adventure"
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60  # Frames per second

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)
SAND_COLOR = (255, 228, 181)

# Font settings
FONT_NAME = "applechancery"
FONT_SIZE = 36
DIALOGUE_FONT_SIZE = 48

# Define font objects
FONT = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
DIALOGUE_FONT = pygame.font.Font(pygame.font.get_default_font(), DIALOGUE_FONT_SIZE)

# Paths to images (if you have image files)
CRUISE_SHIP_IMAGE_PATH = "assets/cruise_ship.png"
ISLAND_MAP_IMAGE_PATH = "assets/island_map.png"
CHARACTER_IMAGES = {
    "john": "assets/john.png",
    "sarah": "assets/sarah.png",
    "alder": "assets/alder.png",
    # Add other characters here
}

# Dialogue
