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
                    self.game_manager.change_scene("island1")  # Move to the cruise ship scene
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

        # Calculate the width of the name text to dynamically adjust the input box size
        text_surface = self.font.render(self.name, True, (213, 213, 255))
        input_box_width = max(600, text_surface.get_width() + 60)  # Ensure minimum width of 600

        # Draw the background rectangle for the input box
        pygame.draw.rect(screen, (42, 42, 138), pygame.Rect(1280 / 4 - 50, 720 / 2 - 80, input_box_width, 100))
        pygame.draw.rect(screen, (65, 65, 138), pygame.Rect(1280 / 4 - 50, 720 / 2 - 80, input_box_width, 100), 5)

        # Draw the label and the name text
        self.font = pygame.font.SysFont("applechancery", 44)

        # Create text with a newline (here we split the text into two lines)
        display_text = f"Enter your name:\n{self.name}"

        # Split the text into lines (splitting by '\n')
        lines = display_text.split('\n')

        # Set starting Y position
        y_offset = 900 / 3

        # Render each line of text
        for line in lines:
            name_text = self.font.render(line, True, (213, 213, 255))
            screen.blit(name_text, (1280 / 4, y_offset))
            y_offset += self.font.get_height()  # Increase the y position for the next line
