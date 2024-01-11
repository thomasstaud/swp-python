import json
from tabulate import tabulate

import game

stats = {}


def print_stats():
    head = ["Sign", "tied", "won", "lost"]
    data = []
    for sign in range(5):
        sign = game.SIGNS[sign]
        data.append([
            sign,
            stats[f"{sign}_tied"],
            stats[f"{sign}_won"],
            stats[f"{sign}_lost"]
        ])

    print(tabulate(data, headers=head, tablefmt="grid"))
    input("Press any key to continue...")


def load_stats():
    global stats

    with open("stats.json", "r") as file:
        stats = json.load(file)


def save_stats():
    json_object = json.dumps(stats, indent=4)
    with open("stats.json", "w") as file:
        file.write(json_object)


def update_stats(sign, result):
    sign = game.SIGNS[sign]
    match result:
        case 0:
            stats[f"{sign}_tied"] += 1
        case 1:
            stats[f"{sign}_won"] += 1
        case 2:
            stats[f"{sign}_lost"] += 1
    save_stats()


def init_stats():
    for sign in game.SIGNS.values():
        stats[f"{sign}_tied"] = 0
        stats[f"{sign}_won"] = 0
        stats[f"{sign}_lost"] = 0


def main():
    init_stats()
    save_stats()


if __name__ == "__main__":
    main()
