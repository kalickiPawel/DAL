import numpy as np
import time


def exercise1(input_matrix, offset_to_add):
    """
    This function adding the offset into declared input matrix
    :param input_matrix: <class 'numpy.ndarray'>
    :param offset_to_add: <class 'int'>
    :return: <class 'numpy.ndarray'> -> new matrix with offset
    """
    return np.vstack((
        np.zeros((offset_to_add, input_matrix.shape[1] + 2 * offset_to_add)),
        np.hstack((
            np.zeros((input_matrix.shape[0], offset_to_add)),
            input_matrix,
            np.zeros((input_matrix.shape[0], offset_to_add)))),
        np.zeros((offset_to_add, input_matrix.shape[1] + 2 * offset_to_add))
    ))


# def exercise1_1(a, offset):
#     '''
#     Alternative version exercise 1
#     '''
#     result = np.zeros((offset*2 + a.shape[0], offset*2 + a.shape[1]))
#     result[offset:a.shape[0]+offset, offset:a.shape[1]+offset] = a
#     return result


def exercise2(n):
    """
    This function generates an output matrix with spiral values
    :param n: <class 'int'>
    :return: <class 'numpy.ndarray'> -> new spiral values matrix
    """
    result = np.zeros((n, n))
    w, k, i = n - 1, 0, 1

    while True:
        while w - 1 >= 0 and result[w - 1, k] == 0:
            result[w, k] = i
            w, i = w - 1, i + 1
        if i >= n ** 2:
            break

        while k + 1 < n and result[w, k + 1] == 0:
            result[w, k] = i
            k, i = k + 1, i + 1
        if i >= n ** 2:
            break

        while w + 1 < n and result[w + 1, k] == 0:
            result[w, k] = i
            w, i = w + 1, i + 1
        if i >= n ** 2:
            break

        while k - 1 >= 0 and result[w, k - 1] == 0:
            result[w, k] = i
            k, i = k - 1, i + 1
        if i >= n ** 2:
            break

    result[w, k] = i
    return result


def exercise3(input_matrix, notch):
    """
    This function notch the values from smaller than -notch and greater than notch.
    Values are changed to 0 but when values are between -notch and notch are changed to 1.
    :param input_matrix: <class 'numpy.ndarray'>
    :param notch: <class 'int'>
    :return: <class 'numpy.ndarray'> -> new matrix with 0s and 1s
    """
    result = np.zeros(input_matrix.shape)
    result[(input_matrix < -notch) | (matrix > notch)] = 1
    return result


def exercise4(input_matrix, notch):
    """
    This function notch the rows where are values smaller than -notch and greater than notch.
    :param input_matrix: <class 'numpy.ndarray'>
    :param notch: <class 'int'>
    :return: <class 'numpy.ndarray'> -> new matrix without rows with values in range from -notch to notch.
    """
    return input_matrix[np.all((input_matrix >= -notch) & (input_matrix <= notch), axis=1)]


def exercise5(*input_matrices):
    """
    This function return vector of unique values from any quantity of matrices
    :param input_matrices: <class 'tuple'>
    :return:<class 'numpy.ndarray'> -> vector with unique matrices values
    """
    result = []
    for m in input_matrices:
        result = np.concatenate((result, np.ravel(m)))
    result = np.unique(result)
    return result


if __name__ == "__main__":
    print("--------------Exercise_1--------------")
    matrix = np.ones((4, 5))
    offset = 2
    print(f"Input: \n{matrix}")
    print(f"Output: \n{exercise1(matrix, offset)}")
    # exercise1_1(a, offset)

    print("--------------Exercise_2--------------")
    n = 5
    print(exercise2(n))

    print("--------------Exercise_3--------------")
    a = 2
    matrix = np.random.randint(-8, 5, (5, 3))
    print(f"Input: \n{matrix}")
    print(f"Output: \n{exercise3(matrix, a)}")

    print("--------------Exercise_4--------------")
    a = 2
    matrix = np.random.randint(-8, 5, (5, 3))
    print(f"Input: \n{matrix}")
    print(f"Output: \n{exercise4(matrix, a)}")

    print("--------------Exercise_5--------------")
    M, N = np.random.randint(-5, 10, (2, 3)), np.random.randint(-30, -20, (4, 2))
    O, P = np.random.randint(15, 30, (3, 2)), np.random.randint(15, 30, (4, 5))
    print(f"Input 1.: \n{M}\nInput 2.: \n{N}\nInput 3.: \n{O}\nInput 4.: \n{P}")
    print(f"Output: \n{exercise5(M, N, O, P)}")
    print(type(exercise5(M, N, O, P)))
