import pygame
import json

class Dialogue:
    def __init__(self, font, screen, dialogue_file, player_name="Player"):
        self.font = font
        self.screen = screen
        self.player_name = player_name  # Store the player's name
        self.is_active = False
        self.current_scene = None
        self.current_message = None

        # Load dialogue JSON file
        with open(dialogue_file, "r", encoding="utf-8") as file:
            self.dialogue_data = json.load(file)

    def start_dialogue(self, scene_name, start_point="start"):
        """Start the dialogue for a specific scene."""
        if scene_name in self.dialogue_data:
            self.current_scene = scene_name
            self.current_message = start_point
            self.is_active = True
        else:
            print(f"Error: Scene '{scene_name}' not found in dialogue data.")

    def advance_dialogue(self):
        """Move to the next message in the dialogue."""
        if not self.is_active or not self.current_scene or not self.current_message:
            return

        current_data = self.dialogue_data[self.current_scene].get(self.current_message, {})
        choices = current_data.get("choices", {})

        if choices:
            # Automatically select the first available choice (for now)
            self.current_message = list(choices.values())[0]
        else:
            self.is_active = False  # End dialogue

    def draw(self):
        """Draw the dialogue and choices on screen."""
        if not self.is_active or not self.current_scene:
            return

        self.screen.fill((255, 255, 255))  # Clear screen

        # Get current dialogue data
        current_data = self.dialogue_data[self.current_scene].get(self.current_message, {})
        text = current_data.get("text", "No dialogue found.")
        speaker = current_data.get("speaker", "Charles")

        # Replace {player} with the actual player's name
        text = text.replace("{player}", self.player_name)

        # Render and display text
        dialogue_text = f"{speaker}: {text}"  # Format as "Tim: Hey Kiera!"
        rendered_text = self.font.render(dialogue_text, True, (0, 0, 0))

        self.screen.blit(rendered_text, (50, 500))

        # Display choices with player's name dynamically added before speech
        choices = current_data.get("choices", {})
        y_offset = 550
        for choice_text, next_message in choices.items():
            # Format the player's response as "Kiera: Hey!"
            formatted_choice = f"{self.player_name}: {choice_text}"
            choice_rendered = self.font.render(formatted_choice, True, (0, 0, 0))
            self.screen.blit(choice_rendered, (50, y_offset))
            y_offset += 40
