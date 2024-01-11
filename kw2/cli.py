import game

PLAY_CMD = 'p'
STAT_CMD = 's'
MENU_CMD = 'exit'


def play():
    sign = None
    while sign not in ['0', '1', '2', '3', '4', 'exit']:
        sign = input(f"\nEnter your sign or enter '{MENU_CMD}' to go back to the menu"
                     "\n(Rock: 0, Paper: 1, Scissors: 2, Spock: 3, Lizard: 4)\n")

    if sign == 'exit':
        menu()

    result = game.play(int(sign), 0)
    if result == 0:
        print("It's a tie!")
    elif result == 1:
        print("You won!")
    else:
        print("You lost!")

    play()


def stats():
    print("\nFeature does not exist yet")
    menu()


def menu():
    print("\nWelcome to: Rock Paper Scissors Spock Lizard - the Game")
    mode = None
    while mode not in [PLAY_CMD, STAT_CMD]:
        mode = input(f"Enter '{PLAY_CMD}' to play or '{STAT_CMD}' for statistics:\n")

    if mode == PLAY_CMD:
        play()
    else:
        stats()


def main():
    menu()


if __name__ == "__main__":
    main()
