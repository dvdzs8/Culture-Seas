import pygame
from dialogue import Dialogue


class IslandMapScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.npcs = ["Alder", "Tara", "Vance"]  # Example NPCs on the island
        self.font = pygame.font.Font(None, 36)
        self.dialogue_system = None

    def enter(self):
        """Called when the scene is first loaded."""
        print("Entered the island map scene")

        # Example dialogue for one NPC (Alder)
        alder_dialogue_data = {
            "start": {
                "text": "Welcome to the island! What brings you here?",
                "choices": {
                    "Tell me about the island": "island_info",
                    "I'm just passing through": "pass_through"
                }
            },
            "island_info": {
                "text": "The island is rich in history, with many old ruins.",
                "choices": {
                    "Tell me more!": "more_info",
                    "Goodbye": "end"
                }
            },
            "end": {
                "text": "Goodbye, traveler!",
                "choices": {}
            }
        }

        self.dialogue_system = Dialogue(self.font, self.game_manager.screen, alder_dialogue_data)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the player clicked on an NPC (e.g., Alder)
                if self.is_npc_clicked("Alder"):
                    self.dialogue_system.start_dialogue()  # Start the dialogue with Alder

    def is_npc_clicked(self, npc_name):
        """Check if an NPC's area was clicked."""
        # Logic for checking if the mouse click is within the bounds of an NPC
        return True  # Simplified for now, assume the NPC was clicked

    def update(self):
        """Update logic for island map scene."""
        if self.dialogue_system.is_active:
            self.dialogue_system.update()

    def draw(self, screen):
        """Draw the island map scene."""
        screen.fill((255, 228, 181))  # Sand-like background
        text = self.font.render("Island Map - Choose an NPC", True, (0, 0, 0))
        screen.blit(text, (100, 50))

        # List NPCs
        for i, npc in enumerate(self.npcs):
            npc_text = self.font.render(npc, True, (0, 0, 0))
            screen.blit(npc_text, (100, 100 + i * 40))

        if self.dialogue_system.is_active:
            # Draw the dialogue interface
            self.dialogue_system.draw()
