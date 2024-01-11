
# Rock, Paper, Scissors, Spock, Lizard = 0, 1, 2, 3, 4
def play(sign_1, sign_2):
    if sign_1 == sign_2:
        return 0
    if ((sign_2 - sign_1) % 5) % 2 == 0:
        return 1
    return 2


def main():
    print(play(0, 1))
    print(play(3, 1))
    print(play(4, 2))
    print(play(0, 4))


if __name__ == "__main__":
    main()
