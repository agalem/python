# -*- coding: utf-8 -*-

'''
Agnieszka Lempaszek
laboratorium 8
'''


def fib_gen():
    '''
    funkcja zwraca kolejne wartości ciągu Fibonacciego
    '''
    a = 0
    b = 1
    temp = 0

    while True:
        result = a
        temp = a + b
        a = b
        b = temp
        yield result



def get_values(iterator, n):
    '''
    funkcja zwraca listę n kolejnych wartości pobranych z iteratora, do czasu skończenia wartości
    '''
    lista = []
    while (n > 0):
        n = n - 1
        try:
            lista.append(next(iterator))
        except StopIteration as x:
            break
    return lista
