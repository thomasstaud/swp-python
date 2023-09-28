import random
import matplotlib.pyplot as plt

def lotto(numbers, pulls):
    # pull numbers
    for i in range(pulls):
        index = random.randint(0, 44 - i)
        numbers[index], numbers[44 - i] = numbers[44 - i], numbers[index]

    return numbers[-6:]


if __name__ == "__main__":
    numbers = list(range(1, 46))

    # call method 1 000 000 times and store results
    stats = [0] * 45
    for _ in range(1000000):
        results = lotto(numbers, 6)
        for result in results:
            stats[result - 1] += 1

    # matplotlib
    # bars
    plt.plot(stats)
    plt.show()
    # line
    fig, ax = plt.subplots()
    ax.bar(numbers, stats)
    plt.show()
