from scipy.spatial import KDTree
import numpy as np


def interpolate_knn(xi, x, y, k):
    """
    Funkcja interpolująca, oparta na metodzie k najbliższych sąsiadów
    :param xi: wartość, dla której chcemy dokonać interpolacji
    :param x: macierz argumentówwęzłów interpolacji
    :param y: wektor wartości węzłów interpolacji
    :param k: liczba uwzględnianych sąsiadów
    :return: średnia arytmetyczna z wartości y dla k najbliższych sąsiadów
    """
    tree = KDTree(x)
    res = tree.query(xi, k)

    s = 0
    for i in res[1]:
        s += y[i]
    return s / len(res[1])


def klasyfikuj_kNN(x, xc, yc, k):
    """
    Klasyfikator, oparty na metodzie k najbliższych sąsiadów
    :param x: wartość, dla której chcemy dokonać klasyfikacji
    :param xc: macierz atrybutów wejściowych danych uczących
    :param yc: wektor klas zadanych
    :param k: liczba uwzględnianych sąsiadów
    :return: najczęstsza klasa spośród k najbliższych sąsiadów
    """
    tree = KDTree(xc)
    res = tree.query(x, k)
    u, count = np.unique(np.unique(yc[res[1]]), return_counts=True)
    idx = np.argmax(count)
    return u[idx]


def walidacja(X, Y):
    """
    Funkcja klasyfikatora, która dobierze optymalną
    dla określonego zbioru danych liczbę k sąsiadów,
    za pomocą kroswalidacji metodą minus jednego elementu.
    :param X: zbiór wejściowy
    :param Y: zbiór wyjściowy
    :return: optymalna liczba k sąsiadów,
    :return: dokładność z jaką została dobrana warość,
    :return: pozostałe wyniki
    """
    best_value, best_k, results = 0.0, 0, []
    k_list = (1, 3, 7, 9, 27)
    for k in k_list:
        true_predictions = 0
        for i in range(X.shape[0]):
            X_train, Y_train = np.delete(X, obj=i, axis=0), np.delete(Y, obj=i, axis=0)
            X_test, Y_test = X[i, :], Y[i]
            predicted = klasyfikuj_kNN(X_test, X_train, Y_train, k)
            if predicted == Y_test:
                true_predictions += 1
        result = true_predictions / X.shape[0]
        results.append(result)
        if result > best_value:
            best_value = result
            best_k = k
    return best_k, best_value, results


if __name__ == "__main__":
    '''
    ------------Zadanie 1--------------
    '''
    x = np.loadtxt("./data/dane3d_i.txt")
    y = np.loadtxt("./data/dane3d_o.txt")
    xi, k = (5, 7), 3
    yi = interpolate_knn(xi, x, y, k)
    print(f"Średnia arytmetyczna z wartości y dla {k} najbliższych sąsiadówy wynosi: {yi}")

    '''
    ------------Zadanie 2--------------
    '''
    xc = np.loadtxt("./data/dane_3D_kapitan_i.txt")
    yc = np.loadtxt("./data/dane_3D_kapitan_o.txt")
    x, k = (-21.18, -3.9, -7.3), 3
    klasa = klasyfikuj_kNN(x, xc, yc, k)
    print(f"Wartość najczęstszej klasy spośród {k} najbliższych sąsiadów: {klasa}")

    '''
    ------------Zadanie 3--------------
    '''
    x = np.loadtxt('data/dane_8D_diabet_i.txt')
    y = np.loadtxt('data/dane_8D_diabet_o.txt')
    best_k, best_score, scores = walidacja(x, y)
    print(f"Najlepszy parametr k: {best_k} z dokładnością {best_score}")
    print("Wyniki: ", scores)
