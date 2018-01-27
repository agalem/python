'''
Laboratorium 9
Agnieszka Lempaszek
moduł matematyczne
'''

def dodawanie(*args):
    '''
    Funkcja pobierająca listę lub liczby, zwracająca sumę
    '''
    suma = 0
    for arg in args:
        if (type(arg) is list):
            for x in arg:
                if(type(x) is int) or (type(x) is float):
                    suma += x
                else:
                    return ("Argumentami muszą być liczby")
        elif (type(arg) is int) or (type(arg) is float):
            suma += arg
        else:
            return ("Argumentami muszą być liczby")
    return suma


def mnozenie(*args):
    '''
    Funkcja przyjmująca liczbę lib listę, zwraca albo iloczyn liczb
     ( w przypadku liczby), albo elementy listy przemnożone przez liczbę
    '''
    if len(args) > 1:
        if (type(args[0]) is list) and (type(args[1]) is int or type(args[1]) is float):
            return [args[1] * arg for arg in args[0]]
        elif (type(args[0]) is int or type(args[0]) is float) and (type(args[1]) is list):
            return [args[0] * arg for arg in args[1]]


    iloczyn = 1

    for arg in args:
        if type(arg) is not list:
            iloczyn *= arg
        else:
            for x in arg:
                iloczyn *= x

    return iloczyn

