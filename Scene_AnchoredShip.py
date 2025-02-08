import pygame

class LoadingScreen:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 48)
        self.loading = True

    def enter(self):
        """Called when the loading scene is first loaded."""
        self.loading = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.game_manager.change_scene("island_map")  # Proceed to the island map

    def update(self):
        """Update the loading screen."""
        if self.loading:
            print("Loading...")  # Placeholder for a loading animation or process

    def draw(self, screen):
        """Draw the loading screen."""
        screen.fill((255, 255, 255))  # White background
        loading_text = self.font.render("Loading...", True, (0, 0, 0))
        screen.blit(loading_text, (540, 320))

