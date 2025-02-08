import pygame

class Dialogue:
    def __init__(self, font, screen, dialogue_data):
        self.font = font
        self.screen = screen
        self.dialogue_data = dialogue_data
        self.current_message = "start"  # Starting point of dialogue
        self.is_active = False
        self.character_portrait = None  # Placeholder for character portraits
        self.dialogue_history = []  # History to keep track of past dialogue

    def enter(self):
        print("Entered the dialogue map scene")

    def start_dialogue(self):
        """Start the dialogue with the NPC."""
        self.is_active = True

    def handle_events(self):
        """Handle player input during dialogue."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.advance_dialogue()

    def advance_dialogue(self):
        """Move to the next message in the dialogue."""
        current_data = self.dialogue_data[self.current_message]
        choices = current_data.get("choices", {})

        if choices:
            # If there are choices, move to the next dialogue based on the first choice
            # In a more complex system, you can use button presses or selections to choose the path.
            self.current_message = list(choices.values())[0]  # Simple auto-choice for now
        else:
            self.is_active = False  # End the dialogue when no more choices

    def update(self):
        """Update logic for the dialogue system."""
        pass

    def draw(self):
        """Draw the dialogue and options on screen."""
        if self.is_active:
            # Clear screen before drawing new text
            self.screen.fill((255, 255, 255))  # White background

            # Get current message to display
            current_message = self.dialogue_data[self.current_message]["text"]

            # Render the current message
            text_surface = self.font.render(current_message, True, (0, 0, 0))
            self.screen.blit(text_surface, (50, 500))  # Position text

            # Draw the choices if available
            choices = self.dialogue_data[self.current_message].get("choices", {})
            y_offset = 550  # Starting position for choices
            for choice, next_message in choices.items():
                choice_text = self.font.render(choice, True, (0, 0, 0))
                self.screen.blit(choice_text, (50, y_offset))
                y_offset += 40  # Move down for the next option

    def get_current_speaker(self):
        """Return the current speaker based on the dialogue (if needed)."""
        return "NPC"  # Just an example, this could be dynamic based on the character

    def display_portrait(self):
        """Display the character portrait of the current speaker (if applicable)."""
        # You can load the character portrait image based on the current speaker
        pass

