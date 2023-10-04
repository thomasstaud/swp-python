import random
import matplotlib.pyplot as plt


def lotto(numbers, draws):
    if draws == 0:
        return []

    num_len = len(numbers)
    # pull numbers
    for i in range(draws):
        index = random.randint(0, (num_len - 1) - i)
        numbers[index], numbers[(num_len - 1) - i] = numbers[(num_len - 1) - i], numbers[index]

    return numbers[-draws:]


if __name__ == "__main__":
    num_len = 45
    draws = 6

    numbers = list(range(1, num_len + 1))

    # call method 1 000 000 times and store results
    stats = [0] * num_len
    for _ in range(1000000):
        results = lotto(numbers, draws)
        for result in results:
            stats[result - 1] += 1

    # matplotlib
    # bars
    plt.plot(stats)
    plt.title("draws per number at 1 000 000 draws")
    plt.xlabel("number")
    plt.ylabel("draws")
    plt.show()
    # line
    fig, ax = plt.subplots()
    ax.bar(numbers, stats)
    plt.title("draws per number at 1 000 000 draws")
    plt.xlabel("number")
    plt.ylabel("draws")
    plt.show()
