from ai.dm import DungeonMaster
from game.character import Character
from game.game_state import GameState


def main():
    dm = DungeonMaster()
    conversation_history = []

    character = Character(
    name="Olberic",
    race="Human",
    character_class="Fighter",
    level=1,
    max_hp=15,
    armor_class=16,
    strength=16,
    dexterity=12,
    constitution=14,
    intelligence=10,
    wisdom=10,
    charisma=12
    )

    game_state = GameState(character)
    game_state.location = "The Winking Skeever Tavern"
    game_state.time_of_day = "Evening"

    print("==============================")
    print("       DUNGEON MASTER AI")
    print("==============================")
    print("Type 'quit' to exit.")
    print()
    print(character.get_summary())
    print()

    while True:
        player_input = input("> ")

        if player_input.lower() == "quit":
            print("Goodbye!")
            break

        response = dm.respond(player_input, conversation_history, character, game_state)
        conversation_history.append(
            {
                "role": "user",
                "content": player_input
            }
        )

        conversation_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )
        

        print()
        print("DM:", response)
        print()


if __name__ == "__main__":
    main()