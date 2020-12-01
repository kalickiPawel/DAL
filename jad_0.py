from Liczba_wymierna import Liczba_wymierna

if __name__ == "__main__":
    #L = Liczba_wymierna(-3, 32, 64)
    L = Liczba_wymierna(3, 0, 0)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Wyswietlanie liczby")
    print("Liczba: {}".format(L))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("2. Zwracanie formy reprezentacyjnej")
    print("Forma reprezentacyjna: {}".format(repr(L)))
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("3. Porownywanie liczb")
    
    L1 = Liczba_wymierna(2, 2, 4)
    L2 = Liczba_wymierna(0, 10, 4)
    
    print("Czy liczby: {}{} \nsa rowne?: {}".format(
        "\n\t Liczba 1.: {}".format(L1),
        "\n\t Liczba 2.: {}".format(L2),
        'Tak' if L1 == L2 else 'Nie'))
    
    L3 = Liczba_wymierna(-2, 3, 7)
    L4 = Liczba_wymierna(0, -9, 4)

    print("Czy 1. liczba z podanych ponizej: {}{} \njest wieksza?: {}".format(
    "\n\t Liczba 1.: {}".format(L3),
    "\n\t Liczba 2.: {}".format(L4),
    'Tak' if L3 > L4 else 'Nie'))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("4. Wykonywanie podstawowych operacji arytmetycznych: dodawania, odejmowania, mnozenia, dzielenia, potegowania, wartosci bezwzglednej")
    
    L5 = Liczba_wymierna(0, -1, 2)
    L6 = Liczba_wymierna(0, -3, 4)

    print("Operacje sa wykonywane dla dwoch liczb: \n\t{}\n\t{}".format(L5, L6))
    print("Dodawanie: {}".format(L5 + L6))
    print("Odejmowanie: {}".format(L5 - L6))
    print("Mnozenie: {}".format(L5 * L6))
    print("Dzielenie: {}".format(L5 / L6))
    print("Potegowanie: {}".format(L5 ** 2))
    # print(L5 * L6)
    # print(L5 / L6)
    # print(L5 ** L6)

    print("\nOperacja abs:\n")
    
    L7 = Liczba_wymierna(0, 2, 7)
    L8 = Liczba_wymierna(0, -2, 7)

    print("{} -> {}".format(L7, abs(L7))) # Liczba_wymierna(0, 2, 7)
    print("{} -> {}".format(L8, abs(L8))) # Liczba_wymierna(0, 2, 7)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("5. Wyswietlenie formy ulamka niewlasciwego")
    print("Ulamek niewlasciwy: {}/{}".format(*L.get_complex_fraction()))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("6. Konwersja do typow: bool, int, float")
    
    print("\nKonwersja na bool:\n")
    L9 = Liczba_wymierna(0, 2, 7)
    L10 = Liczba_wymierna(1, 0, 7)
    L11 = Liczba_wymierna(0, 0, 1)
    print("{} -> {}".format(L9, bool(L9))) # True
    print("{} -> {}".format(L10, bool(L10))) # True
    print("{} -> {}".format(L11, bool(L11))) # False

    print("\nKonwersja na int:\n")

    L12 = Liczba_wymierna(1, 0, 7)
    L13 = Liczba_wymierna(2, 6, 7)
    L14 = Liczba_wymierna(-2, 6, 7)
    L15 = Liczba_wymierna(2, 8, 7)

    print("{} -> {}".format(L12, int(L12))) # 1
    print("{} -> {}".format(L13, int(L13))) # 2
    print("{} -> {}".format(L14, int(L14))) # -2
    print("{} -> {}".format(L15, int(L15))) # 3

    print("\nKonwersja na float:\n")

    L16 = Liczba_wymierna(0, 3, 4)
    L17 = Liczba_wymierna(0, -3, 4)
    L18 = Liczba_wymierna(2, 3, 4)
    L19 = Liczba_wymierna(-2, 3, 4)

    print("{} -> {}".format(L16, float(L16))) # 3/4
    print("{} -> {}".format(L17, float(L17))) # -3/4
    print("{} -> {}".format(L18, float(L18))) # 2 + 3/4
    print("{} -> {}".format(L19, float(L19))) # -2 -3/4

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("7. Zaokraglanie za pomoca funkcji: round.")

    L1 = Liczba_wymierna(0, 3, 4)
    print("Zaokraglana do 1 liczba: {}\n ->: {}".format(L1, round(L1, 1))) # 0.8

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    