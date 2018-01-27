# -*- coding: utf-8 -*-

'''
Agnieszka Lempaszek
laboratorium 11
'''

import math

class SquaresGen:
    """Generator kwadratów kolejnych liczb naturalnych.
           Maksymalną liczbę wyrazów określa 'limit'.
    """
    def __init__(self, limit):
        self.count = 0
        self.limit = limit

    def __iter__(self):
        return SquaresGenNext(self.limit)


class SquaresGenNext(SquaresGen):

    def __next__(self):
        "Zwraca kolejny element ciągu"
        self.count += 1
        if self.count > self.limit:
            raise StopIteration
        return self.count ** 2


class Vector:
    "Wektor w trójwymiarowej przestrzeni euklidesowej."
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        "Wyświetlanie wektora"
        return '[%.2f, %.2f, %.2f]' % (self.x, self.y, self.z)

    def __add__(self, vec):
        "suma: self + vec"
        return Vector(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    ## def __iadd__(self, vec):
    ##     "suma: self += vec"
    ##     self.x += vec.x
    ##     self.y += vec.y
    ##     self.z += vec.z
    ##     return self

    def __mul__(self, vec):
        "mnożenie: self * vec"
        new = Vector(self.x * vec.x, self.y * vec.y, self.z * vec.z)
        return new.x + new.y + new.z

    def __eq__(self, vec):
        "Porównanie wektorów"
        return self.x == vec.x and self.y == vec.y and self.z == vec.z

    def __ne__(self, vec):
        "Sprawdzanie czy wektory nie są równe"
        return not self == vec

    def norm(self):
        "metoda zwracająca normę (długość) wektora"
        sum = ((self.x)**2) + ((self.y)**2) + ((self.z)**2)
        return math.sqrt(sum)

    def __bool__(self):
        "Sprawdzenie czy długość wektora jest niezerowa"
        return self.norm() != 0


class Point:
    "Punkt w trójwymiarowej przestrzeni euklidesowej."
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        "Reprezentacja punktu"
        return '(%.2f, %.2f, %.2f)' % (self.x, self.y, self.z)

    def __sub__(self, point):
        "Odejmowanie dwóch punktów. Zwraca wektor"
        return Vector(self.x - point.x, self.y - point.y, self.z - point.z)

    def __add__(self, vec):
        "suma: self + vec"
        return Point(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def __iadd__(self, vec):
        "Przesunięcie punktu"
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z
        return self

    def __eq__(self, point):
        "Sprawdza czy dwa punkty są takie same"
        return self.x == point.x and self.y == point.y and self.z == point.z

    def __ne__(self, point):
        "Jeżeli dwa punkty są różne"
        return not self == point


class Triangle:
    "Trójkąt w trójwymiarowej przestrzeni euklidesowej."
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __repr__(self):
        "Reprezentacja trójkąta"
        return 'triangle: %s, %s, %s' % (self.A, self.B, self.C)

    def perimeter(self):
        "Oblicza obwód podanego trójkąta"
        self.AB = math.sqrt(((self.B.x - self.A.x)**2) + ((self.B.y - self.A.y)**2) + ((self.B.z - self.A.z)**2))
        self.BC = math.sqrt(((self.C.x - self.B.x)**2) + ((self.C.y - self.B.y)**2) + ((self.C.z - self.B.z)**2))
        self.CA = math.sqrt(((self.A.x - self.C.x)**2) + ((self.A.y - self.C.y)**2) + ((self.A.z - self.C.z)**2))

        return self.AB + self.BC + self.CA

    def area(self):
        "Oblicza pole powierzchni trójkąta wykorzystując wzór Herona"
        p = (self.perimeter())/2
        s = p * (p - self.AB) * (p - self.BC) * (p - self.CA)
        return math.sqrt(s)

    def __eq__(self, triangle):
        "Sprawdza czy dwa trójkąty są takie same"
        wyst= []
        wyst.append(triangle.A)
        wyst.append(triangle.B)
        wyst.append(triangle.C)
        if self.A in wyst:
            wyst.remove(self.A)
        if self.B in wyst:
            wyst.remove(self.B)
        if self.C in wyst:
            wyst.remove(self.C)
        return len(wyst) == 0

    def __ne__(self, triangle):
        "Jeśli dwa trójkąty są różne"
        return not self == triangle