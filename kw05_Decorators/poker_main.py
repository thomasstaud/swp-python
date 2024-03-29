import random

import poker_combinations as poker

ITERATIONS = 10_000
COLORS = 4
SYMBOLS = 13
DRAW_COUNT = 6


def main():
    cards = list(range(0, COLORS * SYMBOLS))

    for _ in range(ITERATIONS):
        random.shuffle(cards)
        draw = cards[:DRAW_COUNT]
        poker.check_combinations(draw, SYMBOLS)

    print(poker.times)
    for key, val in poker.times.items():
        print(f"{key}: {val/ITERATIONS}s")


if __name__ == "__main__":
    main()
