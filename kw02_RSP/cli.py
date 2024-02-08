import random
import game
import statistics

PLAY_CMD = 'p'
STAT_CMD = 's'
MENU_CMD = 'exit'


def play():
    sign = None
    while sign not in ['0', '1', '2', '3', '4', 'exit']:
        print(f"\nEnter your sign or enter '{MENU_CMD}' to go back to the menu")
        print("(Rock: 0, Paper: 1, Scissors: 2, Spock: 3, Lizard: 4)")
        sign = input()

    if sign == 'exit':
        menu()

    sign = int(sign)
    com_sign = random.randint(0, 4)
    print(f"{game.SIGNS[sign]} vs. {game.SIGNS[com_sign]}:")

    result = game.play(sign, com_sign)
    statistics.update_stats(sign, result)
    match result:
        case 0:
            print("It's a tie!")
        case 1:
            print("You won!")
        case 2:
            print("You lost!")

    play()


def stats():
    statistics.print_stats()
    menu()


def menu():
    print("\nWelcome to: Rock Paper Scissors Spock Lizard - the Game")
    mode = None
    while mode not in [PLAY_CMD, STAT_CMD]:
        print(f"Enter '{PLAY_CMD}' to play or '{STAT_CMD}' for statistics:")
        mode = input()

    if mode == PLAY_CMD:
        play()
    else:
        stats()


def main():
    statistics.load_stats()
    menu()


if __name__ == "__main__":
    main()
