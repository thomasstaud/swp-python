import matplotlib.pyplot as plt


def make_chart(stats):
    plt.bar(range(len(stats)), list(stats.values()), align='center')
    plt.xticks(range(len(stats)), list(stats.keys()))
    plt.show()
