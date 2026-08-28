class GameState:

    def __init__(self, character):

        self.character = character

        self.location = "Unknown"
        self.time_of_day = "Unknown"

        self.current_quest = None

        self.npcs = []
        self.inventory = []

    def get_summary(self):

        return (
            f"LOCATION: {self.location}\n"
            f"TIME: {self.time_of_day}\n"
            f"CURRENT QUEST: {self.current_quest}\n"
            f"NPCS: {self.npcs}\n"
            f"INVENTORY: {self.inventory}"
        )