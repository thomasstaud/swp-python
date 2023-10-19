import random


def poker_draw(draw, colors, symbols):
    draw.sort()
    print(draw)

    # get lists of colors and symbols
    color_draws = []
    symbol_draws = []
    for card in draw:
        color_draws.append(card // symbols)
        symbol_draws.append(card % symbols)
    symbol_draws.sort()

    # check if colors are the same
    flush = color_draws[0] == color_draws[-1]
    # check if it is a straight
    # TODO: let straights loop around
    straight = symbol_draws[-1] - symbol_draws[0] == len(symbol_draws)

    # return correct combination
    if flush and straight and (symbol_draws[-1] == (symbols - 1)):
        return "royal_flush"
    elif flush and straight:
        return "straight_flush"
    elif flush:
        return "flush"
    elif straight:
        return "straight"


def poker_stats(cards_num, colors, symbols):
    # generate cards
    cards = list(range(0, colors*symbols))

    for _ in range(iterations):
        random.shuffle(cards)
        draw = cards[:cards_num]

        print(poker_draw(draw, colors, symbols))


if __name__ == "__main__":
    iterations = 3
    cards_num = 5
    colors = 4
    symbols = 13

    poker_stats(cards_num, colors, symbols)
