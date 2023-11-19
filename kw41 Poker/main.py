import sys

import poker_stats
import poker_chart


def main():
    draw_count = 5
    color_count = 4
    symbol_count = 13

    iterations = 100000
    if len(sys.argv) > 1:
        iterations = int(sys.argv[1])

    stats = poker_stats.get_stats(draw_count, color_count, symbol_count, iterations)
    print(stats)
    poker_chart.make_chart(stats)


if __name__ == "__main__":
    main()
