import pygame

class Dialogue:
    def __init__(self, font, screen, dialogue_file, player_name="Player", npc_name="NPC"):
        self.font = font
        self.screen = screen
        self.player_name = player_name
        self.npc_name = npc_name  # Store NPC name
        self.is_active = False
        self.current_scene = None
        self.current_message = None
        self.buttons = []

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

    def advance_dialogue(self, choice=None):
        """Move to the next message in the dialogue based on player's choice."""
        if not self.is_active or not self.current_scene or not self.current_message:
            return

        current_data = self.dialogue_data[self.current_scene].get(self.current_message, {})
        choices = current_data.get("choices", {})

        if choices:
            if choice:
                self.current_message = choices.get(choice)
            else:
                self.current_message = list(choices.values())[0]
            self.buttons.clear()
        else:
            self.is_active = False

    def create_buttons(self, choices):
        """Create buttons for each choice with increased spacing."""
        y_offset = 550
        self.buttons = []

        for choice_text, next_message in choices.items():
            button = Button(self.screen, self.font, f"{self.player_name}: {choice_text}", 50, y_offset, next_message)
            self.buttons.append(button)
            y_offset += 70

    def draw(self):
        """Draw the dialogue and options on screen."""
        if self.is_active:
            # Clear screen before drawing new text
            self.screen.fill((255, 255, 255))  # White background

        pygame.draw.rect(self.screen, (42, 42, 138), pygame.Rect(0, 450, 1280, 300))
        current_data = self.dialogue_data[self.current_scene].get(self.current_message, {})
        text = current_data.get("text", "No dialogue found.")
        speaker = current_data.get("speaker", self.npc_name)  # Use dynamic speaker name

        # Replace {player} with actual player's name, and {npc} with NPC name
        text = text.replace("{player}", self.player_name).replace("{npc}", self.npc_name)

        dialogue_text = f"{speaker}: {text}"
        rendered_text = self.font.render(dialogue_text, True, (0, 0, 0))

    def display_portrait(self):
        """Display the character portrait of the current speaker (if applicable)."""
        # You can load the character portrait image based on the current speaker
        pass

        choices = current_data.get("choices", {})
        if choices:
            self.create_buttons(choices)

        for button in self.buttons:
            button.draw()

    def handle_event(self, event):
        """Handle events such as button clicks."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    self.advance_dialogue(button.next_message)


class Button:
    def __init__(self, screen, font, text, x, y, next_message):
        self.screen = screen
        self.font = font
        self.text = text
        self.x = x
        self.y = y
        self.width = 400
        self.height = 50
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.next_message = next_message

    def draw(self):
        """Draw the button with a background and border."""
        pygame.draw.rect(self.screen, (200, 200, 200), self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 3)
        rendered_text = self.font.render(self.text, True, (0, 0, 0))

        # Center text within the button
        text_x = self.rect.x + (self.width - rendered_text.get_width()) // 2
        text_y = self.rect.y + (self.height - rendered_text.get_height()) // 2
        self.screen.blit(rendered_text, (text_x, text_y))
