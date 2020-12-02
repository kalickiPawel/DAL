import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten, kmeans, kmeans2

from sympy import symbols, Eq, solve
from scipy.optimize import minimize, fsolve
from scipy.integrate import trapz


def exercise1():
    print("Exercise 1 ---------Started---------")
    t1 = time.time()
    x, y, z = symbols('x y z')
    eq1 = Eq(5 * (x ** -1) - 2 * (y ** -1) + 3 * (z ** -1), (-9 / 4))
    eq2 = Eq(2 * (x ** -1) + 3 * (y ** -1) + 1 * (z ** -1), (5 / 12))
    eq3 = Eq(1 * (x ** -1) + 4 * (y ** -1) - 2 * (z ** -1), (5 / 3))

    print(f'{eq1}\n{eq2}\n{eq3}')
    t2 = time.time()
    print(f'Exercise 1 ----------DONE----------- [TIME: {t2 - t1}s]')
    return solve((eq1, eq2, eq3), (x, y, z))


def exercise2():
    print("Exercise 2 ---------Started---------")
    t1 = time.time()

    cons = (
        {'type': 'ineq', 'fun': lambda x: -x[0]},
        {'type': 'ineq', 'fun': lambda x: -x[1]},
        {'type': 'ineq', 'fun': lambda x: x[1] + x[0] + 3}
    )

    result_min = minimize(
        lambda x: x[0] ** 2 + x[1] ** 2 - x[0] * x[1] + x[0] + x[1],
        (-1, -2),
        method='SLSQP',
        constraints=cons
    )
    result_max = minimize(
        lambda x: -(x[0] ** 2 + x[1] ** 2 - x[0] * x[1] + x[0] + x[1]),
        (-1, -2),
        method='SLSQP',
        constraints=cons
    )

    print(f'Punkt: {result_min.x}, Wartosc min:{result_min.fun}')
    print(f'Punkt: {result_max.x}, Wartosc max:{-result_max.fun}')

    t2 = time.time()
    print(f'Exercise 2 ----------DONE----------- [TIME: {t2 - t1}s]')
    return result_min.fun, -result_max.fun


def exercise3():
    print("Exercise 3 ---------Started---------")
    t1 = time.time()

    cons = (
        {'type': 'ineq', 'fun': lambda x: 4 - x[0] ** 2 - x[1] ** 2}
    )

    result_min = minimize(
        lambda x: -((4 - x[0] ** 2 - x[1] ** 2) ** 1 / 2),
        (1, 1),
        method='SLSQP',
        constraints=cons
    )

    result_max = minimize(
        lambda x: (4 - x[0] ** 2 - x[1] ** 2) ** 1 / 2,
        (1, 1),
        method='SLSQP',
        constraints=cons
    )

    print(f'Punkt: {result_min.x}, Wartosc min:{result_min.fun}')
    print(f'Punkt: {result_max.x}, Wartosc max:{-result_max.fun}')

    t2 = time.time()
    print(f'Exercise 3 ----------DONE----------- [TIME: {t2 - t1}s]')
    return result_min.fun, -result_max.fun


def exercise4():
    print("Exercise 4 ---------Started---------")
    t1 = time.time()

    f, g, h = lambda arg: -arg + 1, lambda arg: arg ** 2 - 1, lambda arg: np.sin(arg)

    x0 = fsolve(lambda arg: g(arg) - h(arg), [-0.5])
    x1 = fsolve(lambda arg: f(arg) - h(arg), [0.5])
    x2 = fsolve(lambda arg: f(arg) - g(arg), [0.5])

    int_step = 0.001
    xx1, xx2 = np.arange(x0, x1, int_step), np.arange(x1, x2, int_step)

    A = trapz(h(xx1) - g(xx1), xx1, int_step) + trapz(f(xx2) - g(xx2), xx2, int_step)

    C = trapz(
        (h(xx1) + g(xx1)) / 2 * (h(xx1) - g(xx1)), xx1, int_step
    ) + trapz(
        (f(xx2) + g(xx2)) / 2 * (f(xx2) - g(xx2)), xx2, int_step
    )

    y_cm = 1 / A * C

    print("Moment centralny: " + str(y_cm))

    t2 = time.time()
    print(f'Exercise 4 ----------DONE----------- [TIME: {t2 - t1}s]')
    return y_cm


def exercise5():
    print("Exercise 5 ---------Started---------")
    T1 = time.time()

    print("Dane 2D ---------Started---------")
    t1 = time.time()
    M = np.loadtxt('dane_2D.txt')
    centroid_2d, label_2d = kmeans2(M, 2)
    print(centroid_2d)

    plt.scatter(M[:, 0], M[:, 1], marker='o', c=label_2d)
    plt.plot(centroid_2d[:, 0], centroid_2d[:, 1], 'g*')
    plt.title("dane_2D.txt")
    plt.show()
    t2 = time.time()
    print(f'Dane 2D ----------DONE----------- [TIME: {t2 - t1}s]')

    print("Dane 3D ---------Started---------")
    t1 = time.time()
    M = np.loadtxt('dane_3D.txt')
    centroid_3d, label_3d = kmeans2(M, 3)
    print(centroid_3d)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(M[:, 0], M[:, 1], M[:, 2], marker='o', c=label_3d)
    ax.plot(centroid_3d[:, 0], centroid_3d[:, 1], centroid_3d[:, 2], 'g*')
    plt.title("dane_3D.txt")
    plt.show()
    t2 = time.time()
    print(f'Dane 3D ----------DONE----------- [TIME: {t2 - t1}s]')

    T2 = time.time()
    print(f'Exercise 5 ----------DONE----------- [TIME: {T2 - T1}s]')
    return centroid_2d, centroid_3d


if __name__ == "__main__":
    print(f'result: \n{exercise1()}')
    print(f'result: \n{exercise2()}')
    print(f'result: \n{exercise3()}')
    print(f'result: \n{exercise4()}')
    exercise5 = exercise5()
    print(f'result: \n{exercise5[0]}\n{exercise5[1]}')
