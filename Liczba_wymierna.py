class Liczba_wymierna:
    def __init__(self, integer_part, numerator, denominator):
        
        if denominator < 0:
            raise ValueError("Mianownik musi byc dodatni")
        elif denominator == 0:
            if numerator == 0:
                n = None
                d = None
            else:
                raise ValueError("Licznik musi byc dodatni")
        
        if integer_part:
            if integer_part > 0:
                n = integer_part * denominator + numerator
                d = denominator
            elif integer_part < 0:
                n = integer_part * denominator - numerator
                d = denominator
            else:
                if n and d == None:
                    print('Liczba jest zerem')
                else:
                    raise ValueError("WTF!")
        else:
            n = numerator
            d = denominator

        self.__numerator = n
        self.__denominator = d

        self.integer_part, self.numerator, self.denominator = self.convert_to_mixed_num(self.__numerator, self.__denominator)


    def __str__(self):
        return "Ulamek niewlasciwy: {}/{} Czesc calkowita: {} czesc ulamkowa: {}/{}".format(
            self.__numerator,
            self.__denominator, 
            self.integer_part, 
            self.numerator, 
            self.denominator)
    
    def __repr__(self):
        return "RationalNumber({},{},{})".format(
            self.integer_part, 
            self.numerator, 
            self.denominator)
    
    @staticmethod
    def convert_to_mixed_num(n, d):
        integer_part = int(float(n) / float(d))
        numerator = n - (integer_part * d)
        if n < 0:
            numerator = abs(numerator)
        return integer_part, numerator, d

    def __add__(self, other):
        pass
        # new_c = self.c + other.c
        # self.check_m
        # self.check_
        # if self.m != other.m:

        # return Liczba_wymierna(new_c, new_l, new_m)