import pygame
import pytmx
from dialogue import Dialogue


class IslandMapScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.font = pygame.font.Font(None, 36)
        self.dialogue_system = None

        # Single NPC setup
        self.npc_name = "Adelle"
        self.npc_position = (320, 128)  # Set a fixed position for the NPC
        self.npc_sprite = pygame.image.load("assets/adelle.png")  # Load NPC sprite

        self.player_name = "[NAME]"
        self.player_position = pygame.Vector2(128, 576)
        self.player_sprite = pygame.image.load("assets/Char.png")

        self.tile_size = 32  # Tile size (32x32)
        self.sprite_size = 64
        self.player_speed = 1
        self.player_image = pygame.Surface((64, 64))
        self.player_image.fill((0,0, 255))
        self.move_delay = 200  # Milliseconds between moves
        self.last_move_time = 0  # Store the last movement time

        self.tmx_data = pytmx.load_pygame("assets/island1.tmx")
        self.collision_tiles = self.get_collision_tiles()

    def enter(self):
        """Called when the scene is first loaded."""
        print("Entered the island 1 scene")
        # self.dialogue_system = Dialogue(self.font, self.game_manager.screen, "")

    def get_collision_tiles(self):
        """Extract collision tile positions from the TMX file."""
        collision_tiles = set()
        layer_name = "Collision Layer"  # Change this to your collision layer name

        for layer in self.tmx_data.layers:
            if layer.name == layer_name:
                for x, y, gid in layer:
                    if gid != 0:  # Non-zero GIDs are collision tiles
                        collision_tiles.add((x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))
        return collision_tiles

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     # Check if the player clicked on an NPC (e.g., Alder)
            #     if self.is_npc_clicked("Adelle"):
            #         self.dialogue_system.start_dialogue()  # Start the dialogue with Alder

    def is_npc_clicked(self, npc_name):
        """Check if an NPC's area was clicked."""
        # Logic for checking if the mouse click is within the bounds of an NPC
        return True  # Simplified for now, assume the NPC was clicked

    def update(self):
        """Update logic for island map scene."""
        # if self.dialogue_system.is_active:
        #     self.dialogue_system.update()

        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time < self.move_delay:
            return  # Skip movement if delay hasn't passed

        keys = pygame.key.get_pressed()
        moved = False  # Track if movement happens

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            moved = self.move_player(-self.tile_size, 0)
        if keys[pygame.K_d]:
            moved = self.move_player(self.tile_size, 0)
        if keys[pygame.K_w]:
            moved = self.move_player(0, -self.tile_size)
        if keys[pygame.K_s]:
            moved = self.move_player(0, self.tile_size)

        if moved:
            self.last_move_time = current_time

    def move_player(self, dx, dy):
        new_x = self.player_position.x + dx
        new_y = self.player_position.y + dy

        if self.is_walkable(new_x, new_y):
            self.player_position.x = new_x
            self.player_position.y = new_y
            return True

        return False

    def is_walkable(self, x, y):
        player_rect = pygame.Rect(x, y, 64, 64)
        for tile_pos in self.collision_tiles:
            tile_rect = pygame.Rect(tile_pos[0], tile_pos[1], self.tmx_data.tilewidth, self.tmx_data.tileheight)
            if player_rect.colliderect(tile_rect):
                return False  # Collision detected
        return True

    def draw(self, screen):
        """Draw the island map scene."""
        self.draw_background(screen)
        text = self.font.render("Israelisles", True, (0, 0, 0))
        screen.blit(text, (100, 50))

        screen.blit(self.npc_sprite, self.npc_position)
        screen.blit(self.player_sprite, self.player_position)
        # if self.dialogue_system.is_active:
        #     # Draw the dialogue interface
        #     self.dialogue_system.draw()

    def draw_background(self, screen):
        for layer in self.tmx_data.layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, tile in layer:
                    tile_image = self.tmx_data.get_tile_image_by_gid(tile)
                    if tile_image:
                        screen.blit(tile_image, (x*self.tmx_data.tilewidth,y*self.tmx_data.tileheight))
