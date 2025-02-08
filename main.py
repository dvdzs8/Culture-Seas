import pygame
import Scene_Start
import Scene_Island1
import Scene_CruiseShip
import Scene_AnchoredShip
import game_manager


def main():
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Cruise Adventure")

    # Initialize GameManager
    game = game_manager(screen)

    # Create scenes
    scene_start = Scene_Start(game)
    scene_cruise = Scene_CruiseShip(game)
    scene_anchored = Scene_AnchoredShip(game)
    scene_island1 = Scene_Island1(game)

    # Add scenes to GameManager
    game.add_scene("start", scene_start)
    game.add_scene("cruise", scene_cruise)
    game.add_scene("anchor", scene_anchored)
    game.add_scene("island1", scene_island1)

    # Start the game with the first scene
    game.change_scene("start")

    clock = pygame.time.Clock()

    # Main game loop
    while True:
        # Handle events
        game.current_scene.handle_events()

        # Update and draw the current scene
        game.current_scene.update()
        game.current_scene.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


if __name__ == "__main__":
    main()

