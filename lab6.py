# -*- coding: utf-8 -*-

"""
Laboratorium 6
Agnieszka Lempaszek
"""

a = 10

def print_global():
    """
    Zwraca wartość zmienniej globalnej a
    """

    print(a)


def shadow_a():
    """
    Przypisuje wartość a do zmiennej lokalnej a oraz wywołuje funkcję inner(), która zwraca wartość zmiennej globalnej a
    """
    a = 20
    def inner():
        """
        Zwraca wartość zmiennej globalnej a
        """
        global a
        print (a)
    inner()


def complicated():
    """
    Funkcja wypisze:
    8
    6
    7

    Najpierw wywołujemy funkcję f1(), która przypisuje do zmiennej lokalnej x wartość 8 (nadpisując przypisaną wcześniej wartość 7) i wywołuje funkcję f2()
    Funkcja f2() wypisuje przypisaną do zmiennej lokalnej x wartość (8), a następnie wywołuje funkcję f0()
    Funkcja f0() przypisuje do zmiennej lokalnej x wartość 6 oraz wypisuje przypisaną do zmiennej lokalnej x wartość (6)
    Funkcja f2() po zakończeniu działania funkcji f0() wypisuje przypisaną do zmiennej lokalnej x wartość pomniejszoną o liczbę 1 (7)
    """
    x = 5
    def f0():
        x = 6
        print(x)
    def f1():
        x = 7
        def f2():
            print(x)
            f0()
            print(x-1)
        x = 8
        f2()
    f1()

counter = 1

def increase_counter(n):
    """
    Zwiększa wartość zmiennej globalnej counter o n
    """
    global counter
    counter += n


def make_dict_adder():
    """
    Tworzy nowy pusty słownik d oraz zwraca funckję add(key, value) dodającą do słownika parę klucz-wartość
    """
    d = {}
    def add(key, value):
        """
        Dodaje elementy - klucz (key) i wartość (value) do słownika
        """
        d.update({key:value})
        print (d)
    return add('klucz', 'wartość')
