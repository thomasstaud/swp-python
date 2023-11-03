import random
import matplotlib.pyplot as plt


def get_colors_and_symbols(draw, symbol_count):
    colors = []
    symbols = []
    for card in draw:
        colors.append(card // symbol_count)
        symbols.append(card % symbol_count)
    symbols.sort()

    return colors, symbols


def analyze_poker_draw(draw, symbol_count):
    draw.sort()

    # get lists of colors and symbols
    colors, symbols = get_colors_and_symbols(draw, symbol_count)

    # check for flush (same color)
    flush = colors[0] == colors[-1]

    # check for straight
    straight = True
    for i in range(len(draw)):
        if symbols[i] != (symbols[0] + i):

            last_card = i == (len(draw)-1)
            highest_card = symbols[i] == (symbol_count-1)
            starts_with_zero = symbols[0] == 0

            if last_card and highest_card and starts_with_zero:
                break
            else:
                straight = False
                break

    # check for royal
    royal = symbols[0] == (symbol_count - len(draw))

    # return correct combination
    if flush and straight and royal:
        return "royal-flush"
    elif flush and straight:
        return "straight-flush"

    # check for pairs, three of a kind, four of a kind
    occurrence_dict = {}
    for symbol in symbols:
        if symbol not in occurrence_dict.keys():
            occurrence_dict[symbol] = 0
        occurrence_dict[symbol] += 1
    occurrences = list(occurrence_dict.values())

    four_of_a_kind = 4 in occurrences
    three_of_a_kind = 3 in occurrences
    two_pair = occurrences.count(2) == 2
    pair = 2 in occurrences

    # return correct combination
    if four_of_a_kind:
        return "four-of-a-kind"
    elif three_of_a_kind and pair:
        return "full-house"
    elif flush:
        return "flush"
    elif straight:
        return "straight"
    elif three_of_a_kind:
        return "three-of-a-kind"
    elif two_pair:
        return "two-pair"
    elif pair:
        return "pair"
    else:
        return "highest-card"


def poker_stats(iterations):
    # generate cards
    cards = list(range(0, color_count * symbol_count))
    stats = {"royal-flush": 0, "straight-flush": 0, "four-of-a-kind": 0, "full-house": 0, "flush": 0, "straight": 0,
             "three-of-a-kind": 0, "two-pair": 0, "pair": 0, "highest-card": 0}

    for _ in range(iterations):
        random.shuffle(cards)
        draw = cards[:draw_count]

        result = analyze_poker_draw(draw, symbol_count)
        stats[result] += 100 / iterations

    return stats


if __name__ == "__main__":
    draw_count = 5
    color_count = 4
    symbol_count = 13

    stats = poker_stats(1000000)
    print(stats)

    plt.bar(range(len(stats)), list(stats.values()), align='center')
    plt.xticks(range(len(stats)), list(stats.keys()))

    plt.show()
