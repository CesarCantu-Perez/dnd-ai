from openai import OpenAI
from config.setting import OPENAI_API_KEY

class DungeonMaster:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def respond(self, player_input):
        response = self.client.responses.create(
            model="gpt-5.6-luna",
            instructions=(
                "You are the Dungeon Master for a fantasy role-playing game. "
                "Describe the world, roleplay NPCs, and react to the player's "
                "actions. Never control the player's character or decide "
                "their actions for them. Keep responses immersive but concise."
            ),
            input=player_input
        )

        return response.output_text