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
    
    print("Czy liczby: {}{} \nsą równe?: {}".format(
        "\n\t Liczba 1.: {}".format(L1),
        "\n\t Liczba 2.: {}".format(L2),
        'Tak' if L1 == L2 else 'Nie'))
    
    L3 = Liczba_wymierna(-2, 3, 7)
    L4 = Liczba_wymierna(0, -9, 4)

    print("Czy 1. liczba z podanych ponizej: {}{} \njest większa?: {}".format(
    "\n\t Liczba 1.: {}".format(L3),
    "\n\t Liczba 2.: {}".format(L4),
    'Tak' if L3 > L4 else 'Nie'))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("4. Wykonywanie podstawowych operacji arytmetycznych: +,−,∗, /, **, abs,")

    L5 = Liczba_wymierna(2, 0, 0)
    L6 = Liczba_wymierna(3, 0, 0)
    print(L5 + L6)
    print(L5 - L6)
    # print(L5 * L6)
    # print(L5 / L6)
    # print(L5.get_complex_fraction())
    # print(L6.get_complex_fraction())
    # print(Liczba_wymierna(0,5,1))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("5. Wyswietlenie formy ulamka niewlasciwego")
    print("Ulamek niewlasciwy: {}/{}".format(*L.get_complex_fraction()))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("6. Konwersja do typow: bool, int, float")
    # TODO: Wyswietlic konwersje do typow

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("7. Zaokraglanie za pomoca funkcji: round.")
    # TODO: Zaokraglanie za pomoca funkcji: round

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    