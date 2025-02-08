import pygame
from game_manager import GameManager
from name_entry import NameEntryScene
from cruise_ship import CruiseShipScene
from loading_screen import LoadingScreen
from island_map import IslandMap


def main():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Cruise Adventure")

    # Initialize GameManager
    game_manager = GameManager(screen)

    # Create scenes
    name_entry_scene = NameEntryScene(game_manager)
    cruise_ship_scene = CruiseShipScene(game_manager)
    loading_screen_scene = LoadingScreen(game_manager)
    island_map_scene = IslandMap(game_manager)

    # Add scenes to GameManager
    game_manager.add_scene("name_entry", name_entry_scene)
    game_manager.add_scene("cruise_ship", cruise_ship_scene)
    game_manager.add_scene("loading", loading_screen_scene)
    game_manager.add_scene("island_map", island_map_scene)

    # Start the game with the first scene
    game_manager.change_scene("name_entry")

    clock = pygame.time.Clock()

    # Main game loop
    while True:
        # Handle events
        game_manager.current_scene.handle_events()

        # Update and draw the current scene
        game_manager.current_scene.update()
        game_manager.current_scene.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()

