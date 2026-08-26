from ai.dm import DungeonMaster


def main():
    dm = DungeonMaster()
    conversation_history = []

    print("==============================")
    print("       DUNGEON MASTER AI")
    print("==============================")
    print("Type 'quit' to exit.")
    print()

    while True:
        player_input = input("> ")

        if player_input.lower() == "quit":
            print("Goodbye!")
            break

        response = dm.respond(player_input, conversation_history)
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