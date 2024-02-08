import random
import functools
import time

import poker_combinations as poker

ITERATIONS = 10_000
COLORS = 4
SYMBOLS = 13
DRAW_COUNT = 6

times = {}


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        if __name__ not in times:
            times[func.__name__] = 0
        times[func.__name__] += run_time/ITERATIONS
        print(times)
        return value

    return wrapper


def main():
    cards = list(range(0, COLORS * SYMBOLS))

    for _ in range(ITERATIONS):
        random.shuffle(cards)
        draw = cards[:DRAW_COUNT]
        poker.check_combinations(draw, SYMBOLS)


if __name__ == "__main__":
    main()
