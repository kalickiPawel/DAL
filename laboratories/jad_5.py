import os
import numpy as np

from scipy.spatial import KDTree
from src.utils import get_project_root

root = get_project_root()


class FifthLab:
    def __init__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 1~~~~~~~~~~~~~~~~~~~~")

        x = np.loadtxt(os.path.join(root, os.path.join('data', 'dane3d_i.txt')))
        y = np.loadtxt(os.path.join(root, os.path.join('data', 'dane3d_o.txt')))
        xi, k = (5, 7), 3
        yi = self.interpolate_knn(xi, x, y, k)
        print(f"The arithmetic mean of the y values for the {k} nearest neighbors is: {yi}")

        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 2~~~~~~~~~~~~~~~~~~~~")

        xc = np.loadtxt(os.path.join(root, os.path.join('data', 'dane_3D_kapitan_i.txt')))
        yc = np.loadtxt(os.path.join(root, os.path.join('data', 'dane_3D_kapitan_o.txt')))
        x, k = (-21.18, -3.9, -7.3), 3
        knn_class = self.classify_knn(x, xc, yc, k)
        print(f"The value of the most common class among {k} nearest neighbors is: {knn_class}")

        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 3~~~~~~~~~~~~~~~~~~~~")

        x = np.loadtxt(os.path.join(root, os.path.join('data', 'dane_8D_diabet_i.txt')))
        y = np.loadtxt(os.path.join(root, os.path.join('data', 'dane_8D_diabet_o.txt')))
        best_k, best_score, scores = self.validation(x, y)
        print(f"The best parameter of k: {best_k} with precision {best_score}")
        print("Results: ", scores)

    @staticmethod
    def interpolate_knn(xi, x, y, k):
        """
        Interpolation function, based on k nearest neighbour algorithm
        :param xi: value to interpolate
        :param x: matrix of interpolation node arguments
        :param y: vector of interpolation node values
        :param k: number of included neighbors
        :return: arithmetic mean of the y values for the k nearest neighbors
        """

        tree = KDTree(x)
        res = tree.query(xi, k)

        s = 0
        for i in res[1]:
            s += y[i]
        return s / len(res[1])

    @staticmethod
    def classify_knn(x, xc, yc, k):
        """
        Classifier, based on k nearest neighbour algorithm
        :param x: value to classify
        :param xc: matrix of the input attributes of the training data
        :param yc: vector of given classes
        :param k: number of included neighbors
        :return: the most common class among the k nearest neighbors
        """

        tree = KDTree(xc)
        res = tree.query(x, k)
        u, count = np.unique(np.unique(yc[res[1]]), return_counts=True)
        idx = np.argmax(count)
        return u[idx]

    def validation(self, x, y):
        """
        A classifier function that will select the optimal one
        for a given data set, the number of k neighbors,
        using the minus one element cross-validation method.
        :param x: input set
        :param y: output set
        :return: optimal number of k neighbors
        :return: precision with which the value was selected
        :return: other results
        """

        best_value, best_k, results = 0.0, 0, []
        k_list = (1, 3, 7, 9, 27)
        for k in k_list:
            true_predictions = 0
            for i in range(x.shape[0]):
                x_train, y_train = np.delete(x, obj=i, axis=0), np.delete(y, obj=i, axis=0)
                x_test, y_test = x[i, :], y[i]
                predicted = self.classify_knn(x_test, x_train, y_train, k)
                if predicted == y_test:
                    true_predictions += 1
            result = true_predictions / x.shape[0]
            results.append(result)
            if result > best_value:
                best_value = result
                best_k = k
        return best_k, best_value, results
