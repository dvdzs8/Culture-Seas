class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        """Add a scene to the GameManager."""
        self.scenes[name] = scene

    def change_scene(self, name):
        """Change to a new scene."""
        if name in self.scenes:
            self.current_scene = self.scenes[name]
            self.current_scene.enter()

    def get_current_scene(self):
        """Get the current active scene."""
        return self.current_scene

