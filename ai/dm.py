from openai import OpenAI
from config.setting import OPENAI_API_KEY
from ai.prompts import DM_SYSTEM_PROMPT

class DungeonMaster:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def respond(self, player_input, conversation_history):
        response = self.client.responses.create(
            model="gpt-5.6-luna",
            instructions=DM_SYSTEM_PROMPT,
            input=conversation_history + [
                {
                    "role": "user",
                    "content": player_input
                }
            ]
        )

        return response.output_text