import random


# functions for all 10 pairs


def poker_stats(cards_num, colors, symbols):
    # generate random cards
    cards = []
    for _ in range(cards_num):
        card = random.randint(0, (colors*symbols)-1)
        cards.append(card)

    # check for combinations


if __name__ == "__main__":
    cards_num = 5
    colors = 4
    symbols = 13
    iterations = 1000

    for _ in range(iterations):
        poker_stats(cards_num, colors, symbols)
