from laboratories.RationalNumber import RationalNumber


class FirstLab:
    # L = RationalNumber(-3, 32, 64)
    L = RationalNumber(3, 0, 0)

    def __init__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~Laboratory No. 1~~~~~~~~~~~~~~~~~~")
        self.exercise_01()
        self.exercise_02()
        self.exercise_03(
            RationalNumber(2, 2, 4),
            RationalNumber(0, 10, 4)
        )
        self.exercise_04(
            RationalNumber(0, -1, 2),
            RationalNumber(0, -3, 4),
            abs_state=False
        )
        self.exercise_04(
            RationalNumber(0, 2, 7),
            RationalNumber(0, -2, 7),
            abs_state=True
        )
        self.exercise_05()
        self.exercise_06(
            RationalNumber(0, 2, 7),
            RationalNumber(1, 0, 7),
            RationalNumber(0, 0, 1),
            RationalNumber(2, 8, 7),
            op_type='bool'
        )
        self.exercise_06(
            RationalNumber(1, 0, 7),
            RationalNumber(2, 6, 7),
            RationalNumber(-2, 6, 7),
            RationalNumber(2, 8, 7),
            op_type='int'
        )
        self.exercise_06(
            RationalNumber(0, 3, 4),
            RationalNumber(0, -3, 4),
            RationalNumber(2, 3, 4),
            RationalNumber(-2, 3, 4),
            op_type='float'
        )
        self.exercise_07(RationalNumber(0, 3, 4))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def exercise_01(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Display number")
        print("Number: {}".format(self.L))

    def exercise_02(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("2. Return a representative form")
        print("Representative form: {}".format(repr(self.L)))

    @staticmethod
    def exercise_03(l1, l2):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("3. Comparison of numbers")

        print("Are numbers: {}{} \nequal?: {}".format(
            "\n\t Number 1.: {}".format(l1),
            "\n\t Number 2.: {}".format(l2),
            'Yes' if l1 == l2 else 'No'))

        print("Is 1. number from below: {}{} \nis greater than: {}?".format(
            "\n\t Number 1.: {}".format(l1),
            "\n\t Number 2.: {}".format(l2),
            'Yes' if l1 > l2 else 'No'))

    @staticmethod
    def exercise_04(l1, l2, abs_state=False):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("4. Performing basic arithmetic operations: \n"
              "addition, subtraction, multiplication, division, factorization, "
              "absolute value")
        if abs_state:
            print("\nOperation abs:\n")
            print("{} -> {}".format(l1, abs(l1)))
            print("{} -> {}".format(l2, abs(l2)))
        else:
            print("Operations are performed for two numbers: \n\t{}\n\t{}".format(l1, l2))
            print("Addition: {}".format(l1 + l2))
            print("Subtraction: {}".format(l1 - l2))
            print("Multiplication: {}".format(l1 * l2))
            print("Division: {}".format(l1 / l2))
            print("Factorization: {}".format(l1 ** 2))

    def exercise_05(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("5. Display improper fraction form")
        print("Improper fraction: {}/{}".format(*self.L.get_complex_fraction()))

    @staticmethod
    def exercise_06(l1, l2, l3, l4, op_type):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("6. Type conversion: bool, int, float")

        if op_type == 'bool':
            print("\nConversion to bool:\n")
            print("{} -> {}".format(l1, bool(l1)))
            print("{} -> {}".format(l2, bool(l2)))
            print("{} -> {}".format(l3, bool(l3)))
            print("{} -> {}".format(l3, bool(l4)))

        if op_type == 'int':
            print("\nConversion to int:\n")
            print("{} -> {}".format(l1, int(l1)))
            print("{} -> {}".format(l2, int(l2)))
            print("{} -> {}".format(l3, int(l3)))
            print("{} -> {}".format(l4, int(l4)))

        if op_type == 'float':
            print("\nConversion to float:\n")
            print("{} -> {}".format(l1, float(l1)))
            print("{} -> {}".format(l2, float(l2)))
            print("{} -> {}".format(l3, float(l3)))
            print("{} -> {}".format(l4, float(l4)))

    @staticmethod
    def exercise_07(l1):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("7. Rounding with a function: round.")
        print("Rounded to 1 number: {}\n ->: {}".format(l1, round(l1, 1)))
