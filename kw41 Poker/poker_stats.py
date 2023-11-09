import poker_combinations
import random


def get_stats(draw_count, color_count, symbol_count, iterations):
    # generate cards
    cards = list(range(0, color_count * symbol_count))
    stats = {"royal-flush": 0, "straight-flush": 0, "four-of-a-kind": 0, "full-house": 0, "flush": 0, "straight": 0,
             "three-of-a-kind": 0, "two-pair": 0, "pair": 0, "highest-card": 0}

    for _ in range(iterations):
        random.shuffle(cards)
        draw = cards[:draw_count]

        result = poker_combinations.check_combinations(draw, symbol_count)
        stats[result] += 100 / iterations

    return stats
