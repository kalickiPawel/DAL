import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def exercise_1():
    print("Started ---------Exercise 1---------")
    x = np.linspace(-np.pi, np.pi, 200)
    f1 = np.cos(x)
    f2 = np.sign(x)
    plt.plot(x, f1, 'k')
    plt.plot(x, f2, 'r')
    plt.legend(['f(x) = cos(x)', 'g(x) = sign(x)'])
    plt.xticks(
        (-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi),
        ("$-\pi$", "$-\\frac{\pi}{2}$", 0, "$\\frac{\pi}{2}$", "$\pi$")
    )
    plt.yticks((-1, 0, 1))
    plt.show()


def exercise_2():
    pass


def exercise_3():
    print("Started ---------Exercise 3---------")
    r_v = [2, 2.5, 3, 3.5, 4, 4.5, 5]
    r = np.random.choice(r_v, size=100)

    ax = plt.gca()
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    counts, _, _ = plt.hist(r, bins=len(r_v), rwidth=0.75, color='g', range=(1.75, 5.25))

    for i in range(len(r_v)):
        plt.annotate(
            str(int(counts[i])), xy=(r_v[i], counts[i]), xytext=(0, 3),
            textcoords='offset points', va='bottom', ha='center'
        )

    plt.xlabel('Oceny')
    plt.ylabel('Liczba ocen')
    plt.show()


def exercise_4():
    print("Started ---------Exercise 4---------")
    x = np.arange(-2, 2, 0.01)

    y1 = -x + 1
    y2 = x ** 2 - 1
    y3 = np.sin(x)

    plt.plot(x, y1, 'r',
             x, y2, 'g',
             x, y3, 'b')

    plt.fill_between(
        x, np.minimum(y1, y3), y2, where=np.minimum(y1, y3) > y2,
        hatch='.', color='orange', alpha=0.7
    )
    plt.legend(['$y < - x + 1$', '$y > x^2 - 1$', '$y < sin(x)$'])
    ax = plt.gca()
    ax.set_ylim((-2, 2))  # limits for y axes
    plt.show()


def exercise_5():
    pass


if __name__ == "__main__":
    exercise_1()
    exercise_3()
    exercise_4()
