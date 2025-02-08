import pygame

class NameEntryScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.name = ""
        self.font = pygame.font.Font(None, 48)

    def enter(self):
        """Called when the scene is first loaded."""
        self.name = ""  # Reset the name when entering the scene

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game_manager.change_scene("cruise_ship")  # Move to the cruise ship scene
                elif event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]
                else:
                    self.name += event.unicode  # Add character to name

    def update(self):
        """Any updates to the scene logic."""
        pass

    def draw(self, screen):
        """Draw the scene."""
        screen.fill((255, 255, 255))  # Blank white background
        name_text = self.font.render(f"Enter your name: {self.name}", True, (0, 0, 0))
        screen.blit(name_text, (100, 100))
