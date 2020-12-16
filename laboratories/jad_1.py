from laboratories.Liczba_wymierna import Liczba_wymierna


class FirstLabo:
    # L = Liczba_wymierna(-3, 32, 64)
    L = Liczba_wymierna(3, 0, 0)

    def __init__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("~~~~~~~~~~~~~~~~~~~Laboratoria nr 1~~~~~~~~~~~~~~~~~~")
        self.exercise_01()
        self.exercise_02()
        self.exercise_03(
            Liczba_wymierna(2, 2, 4),
            Liczba_wymierna(0, 10, 4)
        )
        self.exercise_04(
            Liczba_wymierna(0, -1, 2),
            Liczba_wymierna(0, -3, 4),
            abs_state=False
        )
        self.exercise_04(
            Liczba_wymierna(0, 2, 7),
            Liczba_wymierna(0, -2, 7),
            abs_state=True
        )
        self.exercise_05()
        self.exercise_06(
            Liczba_wymierna(0, 2, 7),
            Liczba_wymierna(1, 0, 7),
            Liczba_wymierna(0, 0, 1),
            Liczba_wymierna(2, 8, 7),
            op_type='bool'
        )
        self.exercise_06(
            Liczba_wymierna(1, 0, 7),
            Liczba_wymierna(2, 6, 7),
            Liczba_wymierna(-2, 6, 7),
            Liczba_wymierna(2, 8, 7),
            op_type='int'
        )
        self.exercise_06(
            Liczba_wymierna(0, 3, 4),
            Liczba_wymierna(0, -3, 4),
            Liczba_wymierna(2, 3, 4),
            Liczba_wymierna(-2, 3, 4),
            op_type='float'
        )
        self.exercise_07(Liczba_wymierna(0, 3, 4))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def exercise_01(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Wyswietlanie liczby")
        print("Liczba: {}".format(self.L))

    def exercise_02(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("2. Zwracanie formy reprezentacyjnej")
        print("Forma reprezentacyjna: {}".format(repr(self.L)))

    @staticmethod
    def exercise_03(l1, l2):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("3. Porownywanie liczb")

        print("Czy liczby: {}{} \nsa rowne?: {}".format(
            "\n\t Liczba 1.: {}".format(l1),
            "\n\t Liczba 2.: {}".format(l2),
            'Tak' if l1 == l2 else 'Nie'))

        print("Czy 1. liczba z podanych ponizej: {}{} \njest wieksza?: {}".format(
            "\n\t Liczba 1.: {}".format(l1),
            "\n\t Liczba 2.: {}".format(l2),
            'Tak' if l1 > l2 else 'Nie'))

    @staticmethod
    def exercise_04(l1, l2, abs_state=False):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("4. Wykonywanie podstawowych operacji arytmetycznych: \n"
              "dodawania, odejmowania, mnozenia, dzielenia, potegowania, "
              "wartosci bezwzglednej")
        if abs_state:
            print("\nOperacja abs:\n")
            print("{} -> {}".format(l1, abs(l1)))
            print("{} -> {}".format(l2, abs(l2)))
        else:
            print("Operacje sa wykonywane dla dwoch liczb: \n\t{}\n\t{}".format(l1, l2))
            print("Dodawanie: {}".format(l1 + l2))
            print("Odejmowanie: {}".format(l1 - l2))
            print("Mnozenie: {}".format(l1 * l2))
            print("Dzielenie: {}".format(l1 / l2))
            print("Potegowanie: {}".format(l1 ** 2))

    def exercise_05(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("5. Wyswietlenie formy ulamka niewlasciwego")
        print("Ulamek niewlasciwy: {}/{}".format(*self.L.get_complex_fraction()))

    @staticmethod
    def exercise_06(l1, l2, l3, l4, op_type):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("6. Konwersja do typow: bool, int, float")

        if op_type == 'bool':
            print("\nKonwersja na bool:\n")
            print("{} -> {}".format(l1, bool(l1)))
            print("{} -> {}".format(l2, bool(l2)))
            print("{} -> {}".format(l3, bool(l3)))
            print("{} -> {}".format(l3, bool(l4)))

        if op_type == 'int':
            print("\nKonwersja na int:\n")
            print("{} -> {}".format(l1, int(l1)))
            print("{} -> {}".format(l2, int(l2)))
            print("{} -> {}".format(l3, int(l3)))
            print("{} -> {}".format(l4, int(l4)))

        if op_type == 'float':
            print("\nKonwersja na float:\n")
            print("{} -> {}".format(l1, float(l1)))
            print("{} -> {}".format(l2, float(l2)))
            print("{} -> {}".format(l3, float(l3)))
            print("{} -> {}".format(l4, float(l4)))

    @staticmethod
    def exercise_07(l1):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("7. Zaokraglanie za pomoca funkcji: round.")
        print("Zaokraglana do 1 liczba: {}\n ->: {}".format(l1, round(l1, 1)))
