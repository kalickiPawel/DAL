from Liczba_wymierna import Liczba_wymierna

if __name__ == "__main__":
    L = Liczba_wymierna(-3, 32, 64)
    print("-----------------------------------------------------")
    print("1. Wyswietlanie liczby")
    print("2. Zwracanie formy reprezentacyjnej")
    print("-----------------------------------------------------")
    
    print("Liczba: {}".format(L))
    print("Forma reprezentacyjna: {}".format(repr(L)))
    
    print("Ulamek niewlasciwy: {}".format(L.get_complex_fraction()))
    print("Czesc calkowita: {}".format(L.get_fration_part()))
    print("Czesc ulamkowa: {}".format(L.get_integer_part()))

    print("-----------------------------------------------------")
    print("3. Porownywanie liczb")
    print("-----------------------------------------------------")
    
    L1 = Liczba_wymierna(2, 2, 4)
    L2 = Liczba_wymierna(0, 10, 4)
    
    print("Czy liczby: {}{} \nsą równe?: {}".format(
        "\n\t Liczba 1.: {}".format(L1),
        "\n\t Liczba 2.: {}".format(L2),
        'Tak' if L1 == L2 else 'Nie'))

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    L3 = Liczba_wymierna(-2, 3, 7)
    L4 = Liczba_wymierna(0, -9, 4)

    print("Czy 1. liczba z podanych ponizej: {}{} \njest większa?: {}".format(
    "\n\t Liczba 1.: {}".format(L3),
    "\n\t Liczba 2.: {}".format(L4),
    'Tak' if L3 > L4 else 'Nie'))

    print("-----------------------------------------------------")
