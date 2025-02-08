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
                    self.game_manager.change_scene("cruise")  # Move to the cruise ship scene
                elif event.key == pygame.K_BACKSPACE:
                    self.name = self.name[:-1]
                else:
                    self.name += event.unicode  # Add character to name


    def update(self):
        """Any updates to the scene logic."""
        pass

    def draw(self, screen):
        """Draw the scene."""
        screen.fill((21, 21, 100))  # Blank background
        pygame.draw.rect(screen, (42, 42, 138), pygame.Rect(1280/4 - 50, 720/2 - 50, 600, 70))
        pygame.draw.rect(screen, (65, 65, 138), pygame.Rect(1280/4 - 50, 720/2 - 50, 600, 70), 5)

        self.font = pygame.font.SysFont("applechancery", 44)

        #name_text = self.font.render(f"Enter your name: \n{self.name}", True, (213, 213, 255))

        # Create text with a newline (here we split the text into two lines)
        display_text = f"Enter your name:\n{self.name}"

        # Split the text into lines (splitting by '\n')
        lines = display_text.split('\n')

        # Set starting Y position
        y_offset = 720 / 3

        # Render each line of text
        for line in lines:
            name_text = self.font.render(line, True, (213, 213, 255))
            screen.blit(name_text, (1280 / 4, y_offset))
            y_offset += self.font.get_height()  # Increase the y position for the next line
