import pygame

class CruiseShipScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.characters = ["John", "Sarah", "Tom"]  # Example characters
        self.font = pygame.font.Font(None, 36)

    def enter(self):
        """Called when the scene is first loaded."""
        print("Entered the cruise ship scene")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Example of handling a click (this could be an interaction with a character)
                print("Clicked on the cruise ship")
                #switch to dialogue screen
                self.game_manager.change_scene("dialogue")

    def update(self):
        """Update logic for cruise ship scene."""
        pass

    def draw(self, screen):
        """Draw the cruise ship scene."""
        screen.fill((173, 216, 230))  # Light blue background for sea
        text = self.font.render("Cruise Ship - Choose a character", True, (0, 0, 0))
        screen.blit(text, (100, 50))
        # List characters
        for i, char in enumerate(self.characters):
            char_text = self.font.render(char, True, (0, 0, 0))
            screen.blit(char_text, (100, 100 + i * 40))

