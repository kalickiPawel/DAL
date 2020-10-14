import math

class Liczba_wymierna:
    def __init__(self, integer_part, numerator, denominator):

        if denominator <= 0 and numerator !=0:
            raise ValueError("Mianownik musi byc dodatni")

        if integer_part and numerator < 0:
            raise ValueError("Licznik musi byc dodatni gdy wystepuje liczba calkowita")
        
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
            n = numerator
            d = denominator
        
        self._numerator = n
        self._denominator = d

        if self._numerator != 0 and self._denominator != 0:
            self.fraction_reduction()
            self.integer_part, self.numerator, self.denominator = self.convert_to_mixed_num(self._numerator, self._denominator)
        else:
            self.integer_part = integer_part
            self.numerator, self.denominator = self.get_complex_fraction()
    

    def __repr__(self):
        if self.integer_part:
            if self.numerator != 0:
                return "Czesc calkowita: {} czesc ulamkowa: {}/{}".format(
                    self.integer_part, 
                    self.numerator, 
                    self.denominator)
            else:
                return "Liczba calkowita: {} brak czesci ulamowej".format(self.integer_part)
        else:
            return "Ulamek zwykly: {}/{} brak liczby calkowitej".format(
                self._numerator,
                self._denominator)
    
    def __str__(self):
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
        if numerator == 0:
            if integer_part != 0: d = 0
            else:
                raise ValueError("Nie mozesz podac tylko mianownika, licznik nie moze byc zerem")
        return integer_part, numerator, d

    def fraction_reduction(self):
        gcd = math.gcd(self._numerator, self._denominator)
        self._numerator = int(self._numerator / gcd)
        self._denominator = int(self._denominator / gcd)
        return self._numerator, self._denominator
        
    def get_complex_fraction(self):
        if self._numerator != 0 and self._denominator != 0:
            return (self._numerator, self._denominator)
        else:
            return (self.integer_part, 1)

    def get_integer_part(self):
        return self.integer_part

    def get_fration_part(self):
        return (self.numerator, self.denominator)

    def __eq__(self, other):
        n1, d1 = self.get_complex_fraction()
        n2, d2 = other.get_complex_fraction()
        return n1 == n2 and d1 == d2

    def __gt__(self, other):
        n1, d1 = self.get_complex_fraction()
        n2, d2 = other.get_complex_fraction()
        return n1/d1 > n2/d2

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        n1, d1 = self.get_complex_fraction()
        n2, d2 = other.get_complex_fraction()
        return n1/d1 < n2/d2

    def __le__(self, other):
        return self < other or self == other

    def __add__(self, other):
        n1, d1 = self.get_complex_fraction()
        n2, d2 = other.get_complex_fraction()
        
        # sprowadzic do wspolnego mianownika
        n1_f = n1 * d2
        d1_f = d1 * d2
        n2_f = n2 * d1
        d2_f = d2 * d1

        return Liczba_wymierna(0, n1_f + n2_f, d1_f)

    def __sub__(self, other):
        n1, d1 = self.get_complex_fraction()
        n2, d2 = other.get_complex_fraction()
        
        # sprowadzic do wspolnego mianownika
        n1_f = n1 * d2
        d1_f = d1 * d2
        n2_f = n2 * d1
        d2_f = d2 * d1

        return Liczba_wymierna(0, n1_f - n2_f, d1_f)

    # def __mul__(self, other):
    #     return Liczba_wymierna(0, self._numerator * other._numerator, self._denominator * other._denominator)
    
    # def __truediv__(self, other):
    #     n, d = other.get_complex_fraction()
    #     if n < 0:
    #         d = -d
    #         n = -n
    #     return self.__mul__(Liczba_wymierna(0, d, n))
    
