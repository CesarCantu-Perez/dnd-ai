from ai.dm import DungeonMaster


def main():
    dm = DungeonMaster()

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

        response = dm.respond(player_input)

        print()
        print("DM:", response)
        print()


if __name__ == "__main__":
    main()