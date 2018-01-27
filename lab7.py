# -*- coding: utf-8 -*-

"""
Laboratorium 6
Agnieszka Lempaszek
"""

def call(fun, *args, **kw_args):
    '''Funkcja wywuołująca dowolną funkcję z dowolnymi argumentami przekazanymi do funkcji'''
    print (fun(*args, **kw_args))


def add_to_dict(key, value, d={}):
    '''Funkcja dodająca parę klucz-wartość do słownika'''
    d[key] = value
    print (d)

