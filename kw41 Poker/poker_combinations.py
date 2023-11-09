def get_colors_and_symbols(draw, symbol_count):
    colors = []
    symbols = []
    for card in draw:
        colors.append(card // symbol_count)
        symbols.append(card % symbol_count)
    symbols.sort()

    return colors, symbols


def check_combinations(draw, symbol_count):
    draw.sort()

    # get lists of colors and symbols
    colors, symbols = get_colors_and_symbols(draw, symbol_count)

    # check for flush (same color)
    flush = colors[0] == colors[-1]

    # check for straight
    # TODO: rewrite
    straight = True
    for i in range(len(draw)):
        if symbols[i] != (symbols[0] + i):

            last_card = i == (len(draw) - 1)
            highest_card = symbols[i] == (symbol_count - 1)
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
