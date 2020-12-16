import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


class ThirdLab:
    def __init__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~Laboratory No. 3~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        self.exercise_1()
        self.exercise_2()
        self.exercise_3()
        self.exercise_4()
        self.exercise_5()
        self.exercise_6()

    @staticmethod
    def exercise_1():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 1~~~~~~~~~~~~~~~~~~~~")
        x = np.linspace(-np.pi, np.pi, 200)
        f1 = np.cos(x)
        f2 = np.sign(x)
        plt.plot(x, f1, 'k')
        plt.plot(x, f2, 'r')
        plt.legend(['f(x) = cos(x)', 'g(x) = sign(x)'])
        plt.xticks((-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi),
                   ("$-\pi$", "$-\\frac{\pi}{2}$", 0, "$\\frac{\pi}{2}$", "$\pi$"))
        plt.yticks((-1, 0, 1))
        plt.show()

    @staticmethod
    def exercise_2():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 2~~~~~~~~~~~~~~~~~~~~")
        b_dots, r_dots = [], []
        coords = np.random.rand(1024, 2) * 1.0

        for i in range(len(coords)):
            a, a_1 = coords[i][1] < 0.33, coords[i][0] > 0.33
            b, b_1 = coords[i][1] > 0.66, coords[i][0] < 0.66
            c, c_1 = coords[i][0] < 0.33, coords[i][1] > 0.33
            d, d_1 = coords[i][0] > 0.66, coords[i][1] < 0.66
            if (c and (a or b)) or (d and (a or b)) or ((a_1 and b_1) and (c_1 and d_1)):
                b_dots.append(coords[i])
            else:
                r_dots.append(coords[i])

        b_dots, r_dots = np.array(b_dots), np.array(r_dots)

        plt.scatter(b_dots[:, 0], b_dots[:, 1], color="b", alpha=0.7)
        plt.scatter(r_dots[:, 0], r_dots[:, 1], color="r", alpha=0.7)

        plt.show()

    @staticmethod
    def exercise_3():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 3~~~~~~~~~~~~~~~~~~~~")
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

        plt.xlabel('Grades')
        plt.ylabel('Count of grades')
        plt.show()

    @staticmethod
    def exercise_4():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 4~~~~~~~~~~~~~~~~~~~~")
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

    @staticmethod
    def exercise_5():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 5~~~~~~~~~~~~~~~~~~~~")
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x, y = np.meshgrid(np.linspace(-2, 2, 50), np.linspace(-2, 2, 50))

        z1 = (1 / (1 + np.e ** (-x - y))) * (x + y >= 0)
        z2 = 0.5 * (x + y < 0)
        z = z1 + z2

        ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='jet', alpha=0.8)
        plt.show()

    @staticmethod
    def exercise_6():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 6~~~~~~~~~~~~~~~~~~~~")
        k, a_val = 200, [2, 2.9, 3, 3.56, 3.6]
        p, q = np.zeros((k, 1)), np.zeros((k, 1))
        p[0], q[0] = 0.1, 0.0001

        fig, ax = plt.subplots(5, 1)
        fig.set_size_inches(8.6, 6.5)
        for item, axes in enumerate(ax):
            a = a_val[item]
            axes.set_title(f"a: {a}")
            for i in range(1, k):
                p[i] = a * p[i - 1] * (1 - p[i - 1])
                q[i] = a * q[i - 1] * (1 - q[i - 1])
            axes.plot(np.arange(k), p, 'r')
            axes.plot(np.arange(k), q, 'g')
            axes.plot(np.arange(k), np.abs(p - q), 'b')
        plt.subplots_adjust(hspace=1.0)
        plt.show()
