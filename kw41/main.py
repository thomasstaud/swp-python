import random


# TODO: functions for all 10 pairs


def poker_draw(draw, colors, symbols):
    print(draw)
    # check for combinations


def poker_stats(cards_num, colors, symbols):
    # generate cards
    cards = list(range(0, colors*symbols))

    for _ in range(iterations):
        random.shuffle(cards)
        poker_draw(cards[:cards_num], colors, symbols)


if __name__ == "__main__":
    iterations = 3
    cards_num = 5
    colors = 4
    symbols = 13

    poker_stats(cards_num, colors, symbols)
