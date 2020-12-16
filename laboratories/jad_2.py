import numpy as np


class SecondLab:
    def __init__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~Laboratory No. 2~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        matrix = np.ones((4, 5))
        offset = 2
        print(f"Output: \n{self.exercise1(matrix, offset)}")
        print(f"Output v2: \n{self.exercise1_1(matrix, offset)}")

        n = 5
        print(f"Output: \n{self.exercise2(n)}")

        a = 2
        matrix = np.random.randint(-8, 5, (5, 3))
        print(f"Output: \n{self.exercise3(matrix, a)}")

        print(f"Output: \n{self.exercise4(matrix, a)}")

        print("Output: \n{}".format(self.exercise5(
            np.random.randint(-5, 10, (2, 3)),
            np.random.randint(-30, -20, (4, 2)),
            np.random.randint(15, 30, (3, 2)),
            np.random.randint(15, 30, (4, 5))
        )))

    @staticmethod
    def exercise1(input_matrix, offset_to_add):
        """
        This function adding the offset into declared input matrix
        :param input_matrix: <class 'numpy.ndarray'>
        :param offset_to_add: <class 'int'>
        :return: <class 'numpy.ndarray'> -> new matrix with offset
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 1~~~~~~~~~~~~~~~~~~~~")
        print(f"Input: \n{input_matrix}")
        return np.vstack((
            np.zeros((offset_to_add, input_matrix.shape[1] + 2 * offset_to_add)),
            np.hstack((
                np.zeros((input_matrix.shape[0], offset_to_add)),
                input_matrix,
                np.zeros((input_matrix.shape[0], offset_to_add)))),
            np.zeros((offset_to_add, input_matrix.shape[1] + 2 * offset_to_add))
        ))

    @staticmethod
    def exercise1_1(a, offset):
        """
        Alternative version exercise 1
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 1~v.2~~~~~~~~~~~~~~~~")
        print(f"Input: \n{a}")
        result = np.zeros((offset*2 + a.shape[0], offset*2 + a.shape[1]))
        result[offset:a.shape[0]+offset, offset:a.shape[1]+offset] = a
        return result

    @staticmethod
    def exercise2(n):
        """
        This function generates an output matrix with spiral values
        :param n: <class 'int'>
        :return: <class 'numpy.ndarray'> -> new spiral values matrix
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 2~~~~~~~~~~~~~~~~~~~~")
        print(f"Input: \n{n}")

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

    @staticmethod
    def exercise3(input_matrix, notch):
        """
        This function notch the values from smaller than -notch and greater than notch.
        Values are changed to 0 but when values are between -notch and notch are changed to 1.
        :param input_matrix: <class 'numpy.ndarray'>
        :param notch: <class 'int'>
        :return: <class 'numpy.ndarray'> -> new matrix with 0s and 1s
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 3~~~~~~~~~~~~~~~~~~~~")
        print(f"Input: \nInput_matrix: \n{input_matrix}\nNotch: \n{notch}")
        result = np.zeros(input_matrix.shape)
        result[(input_matrix < -notch) | (input_matrix > notch)] = 1
        return result

    @staticmethod
    def exercise4(input_matrix, notch):
        """
        This function notch the rows where are values smaller than -notch and greater than notch.
        :param input_matrix: <class 'numpy.ndarray'>
        :param notch: <class 'int'>
        :return: <class 'numpy.ndarray'> -> new matrix without rows with values in range from -notch to notch.
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 4~~~~~~~~~~~~~~~~~~~~")
        print(f"Input: \nInput_matrix: \n{input_matrix}\nNotch: \n{notch}")
        return input_matrix[np.all((input_matrix >= -notch) & (input_matrix <= notch), axis=1)]

    @staticmethod
    def exercise5(*input_matrices):
        """
        This function return vector of unique values from any quantity of matrices
        :param input_matrices: <class 'tuple'>
        :return:<class 'numpy.ndarray'> -> vector with unique matrices values
        """
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 5~~~~~~~~~~~~~~~~~~~~")
        m, n, o, p = input_matrices
        print(f"Input 1.: \n{m}\nInput 2.: \n{n}\nInput 3.: \n{o}\nInput 4.: \n{p}")
        result = []
        for m in input_matrices:
            result = np.concatenate((result, np.ravel(m)))
        result = np.unique(result)
        return result
