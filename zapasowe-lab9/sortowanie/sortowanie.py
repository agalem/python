'''
Laboratorium 9
Agnieszka Lempaszek
moduł sortowanie
'''

def po_pierwszym(l, reverse = False):
    """
    Funkcja sortuje podane obiekty po pierwszym elemencie
    """
    return sorted(l, key = lambda x: x[0], reverse = reverse)

def po_drugim(l, reverse = False):
    """
    Funkcja sortuje podane obiekty po drugim elemencie
    """
    return sorted(l, key = lambda x: x[1], reverse = reverse)