import os
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans2

from sympy import symbols, Eq, solve
from scipy.optimize import minimize, fsolve
from scipy.integrate import trapz

from src.utils import get_project_root

root = get_project_root()


class FourthLab:
    def __init__(self):
        print(f'result: \n{self.exercise1()}')
        print(f'result: \n{self.exercise2()}')
        print(f'result: \n{self.exercise3()}')
        print(f'result: \n{self.exercise4()}')
        exercise5 = self.exercise5()
        print(f'result: \n{exercise5[0]}\n{exercise5[1]}')

    @staticmethod
    def exercise1():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 1~~~~~~~~~~~~~~~~~~~~")
        t1 = time.time()
        x, y, z = symbols('x y z')
        eq1 = Eq(5 * (x ** -1) - 2 * (y ** -1) + 3 * (z ** -1), (-9 / 4))
        eq2 = Eq(2 * (x ** -1) + 3 * (y ** -1) + 1 * (z ** -1), (5 / 12))
        eq3 = Eq(1 * (x ** -1) + 4 * (y ** -1) - 2 * (z ** -1), (5 / 3))

        print(f'{eq1}\n{eq2}\n{eq3}')
        t2 = time.time()
        print(f"~Exercise 1~~~~~~~~~~DONE~~~~~~~~~~[TIME: {t2 - t1}s]")
        return solve((eq1, eq2, eq3), (x, y, z))

    @staticmethod
    def exercise2():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 2~~~~~~~~~~~~~~~~~~~~")
        t1 = time.time()

        cons = (
            {'type': 'ineq', 'fun': lambda x: -x[0]},
            {'type': 'ineq', 'fun': lambda x: -x[1]},
            {'type': 'ineq', 'fun': lambda x: x[1] + x[0] + 3}
        )

        result_min = minimize(
            lambda x: x[0] ** 2 + x[1] ** 2 - x[0] * x[1] + x[0] + x[1],
            np.array([-1, -2]),
            method='SLSQP',
            constraints=cons
        )
        result_max = minimize(
            lambda x: -(x[0] ** 2 + x[1] ** 2 - x[0] * x[1] + x[0] + x[1]),
            np.array([-1, -2]),
            method='SLSQP',
            constraints=cons
        )

        print(f'Point: {result_min.x}, Value min:{result_min.fun}')
        print(f'Point: {result_max.x}, Value max:{-result_max.fun}')

        t2 = time.time()
        print(f"~Exercise 2~~~~~~~~~~DONE~~~~~~~~~~[TIME: {t2 - t1}s]")
        return result_min.fun, -result_max.fun

    @staticmethod
    def exercise3():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 3~~~~~~~~~~~~~~~~~~~~")
        t1 = time.time()

        cons = (
            {'type': 'ineq', 'fun': lambda x: 4 - x[0] ** 2 - x[1] ** 2}
        )

        result_min = minimize(
            lambda x: -((4 - x[0] ** 2 - x[1] ** 2) ** 1 / 2),
            np.array([1, 1]),
            method='SLSQP',
            constraints=cons
        )

        result_max = minimize(
            lambda x: (4 - x[0] ** 2 - x[1] ** 2) ** 1 / 2,
            np.array([1, 1]),
            method='SLSQP',
            constraints=cons
        )

        print(f'Point: {result_min.x}, Value min:{result_min.fun}')
        print(f'Point: {result_max.x}, Value max:{-result_max.fun}')

        t2 = time.time()
        print(f"~Exercise 3~~~~~~~~~~DONE~~~~~~~~~~[TIME: {t2 - t1}s]")
        return result_min.fun, -result_max.fun

    @staticmethod
    def exercise4():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 4~~~~~~~~~~~~~~~~~~~~")
        t1 = time.time()

        f, g, h = lambda arg: -arg + 1, lambda arg: arg ** 2 - 1, lambda arg: np.sin(arg)

        x0 = fsolve(lambda arg: g(arg) - h(arg), np.array([-0.5]))
        x1 = fsolve(lambda arg: f(arg) - h(arg), np.array([0.5]))
        x2 = fsolve(lambda arg: f(arg) - g(arg), np.array([0.5]))

        int_step = 0.001
        xx1, xx2 = np.arange(x0, x1, int_step), np.arange(x1, x2, int_step)

        a = trapz(h(xx1) - g(xx1), xx1, int_step) + trapz(f(xx2) - g(xx2), xx2, int_step)

        c = trapz(
            (h(xx1) + g(xx1)) / 2 * (h(xx1) - g(xx1)), xx1, int_step
        ) + trapz(
            (f(xx2) + g(xx2)) / 2 * (f(xx2) - g(xx2)), xx2, int_step
        )

        y_cm = 1 / a * c

        print("Central moment: " + str(y_cm))

        t2 = time.time()
        print(f"~Exercise 4~~~~~~~~~~DONE~~~~~~~~~~[TIME: {t2 - t1}s]")
        return y_cm

    @staticmethod
    def exercise5():
        data2d_path = os.path.join(root, os.path.join('data', 'dane_2D.txt'))
        data3d_path = os.path.join(root, os.path.join('data', 'dane_3D.txt'))
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 5~~~~~~~~~~~~~~~~~~~~")
        t1_main = time.time()

        print("~~~~~~~~~~~~~~~~~~~Exercise 5 DATA 2D~~~~~~~~~~~~~~~~")
        t1 = time.time()
        m = np.loadtxt(data2d_path)
        centroid_2d, label_2d = kmeans2(m, 2)
        print(centroid_2d)

        plt.scatter(m[:, 0], m[:, 1], marker='o', c=label_2d)
        plt.plot(centroid_2d[:, 0], centroid_2d[:, 1], 'g*')
        plt.title(data2d_path)
        plt.show()
        t2 = time.time()
        print(f"~Exercise 5 DATA 2D~~~~~~DONE~~~~~~[TIME: {t2 - t1}s]")

        print("~~~~~~~~~~~~~~~~~~~Exercise 5 DATA 3D~~~~~~~~~~~~~~~~")
        t1 = time.time()
        m = np.loadtxt(data3d_path)
        centroid_3d, label_3d = kmeans2(m, 3)
        print(centroid_3d)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(m[:, 0], m[:, 1], m[:, 2], marker='o', c=label_3d)
        ax.plot(centroid_3d[:, 0], centroid_3d[:, 1], centroid_3d[:, 2], 'g*')
        plt.title(data3d_path)
        plt.show()
        t2 = time.time()
        print(f"~Exercise 5 DATA 3D~~~~~~DONE~~~~~~[TIME: {t2 - t1}s]")

        t2_main = time.time()
        print(f"~Exercise 4~~~~~~~~~~DONE~~~~~~~~~~[TIME: {t2_main - t1_main}s]")
        return centroid_2d, centroid_3d
