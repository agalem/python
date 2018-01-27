"Laboratorium 5, Agnieszka Lempaszek"

import math

# Zadanie 5.1

def czy_parzyste(x, y):

    for i in range(x, y+1):
        if i % 2 == 0:
            print (i,' parzysta')
        else:
            print (i,' nieparzysta')

    print ('\n')


czy_parzyste(1,5)

# Zadanie 5.2

def czy_pierwsze(x):
    numbers = range(1, x+1)
    primes = [x for x in numbers if all(x % y != 0 for y in range(2, round((x + 2) / 2)))]
    taken = []

    for i in numbers:
        if i in primes:
            numType = ' liczba pierwsza'
            print (i, numType)
        else:
            numType = ' liczba złożona: '
            for j in range(2, x):
                for k in range(2, x):
                    if j * k == i and k not in taken:
                        numType += '%s*%s  ' % (j, k)
                        if j not in taken:
                            taken.append(j)
            print (i, numType)

czy_pierwsze(15)

# Zadanie 5.3

def slownie():

    # s - liczba setek
    # d - liczba dziesiątek
    # j - liczba jedności
    # n - liczba nastek (11-19)
    # w - rząd wielkości
    # f - forma gramatyczna



    jednosci =['', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']
    nascie = ['', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście', 'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście']
    dziesiatki =['', 'dziesięć', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt', 'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']
    setki = ['','sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset', 'sześćset','siedemset', 'osiemset', 'dziewięćset']

    wielkosci = [
        ['', '', ''],
        ['tysiąc', 'tysiące', 'tysięcy'],
        ['milion', 'miliony', 'milionów'],
        ['miliard', 'miliardy', 'miliardów'],
        ['bilion', 'biliony', 'bilionów'],
        ['biliard', 'biliony', 'biliardów'],
        ['trylion', 'tryliony', 'trylionów'],
        ['tryliard', 'tryliony', 'tryliardów'],
        ['kwadrylion', 'kwadryliony', 'kwadrylionów'],
        ['kwadryliard', 'kwadryliardy', 'kwadryliardów'],
        ['kwintylion', 'kwintyliony', 'kwintylionów'],
        ['kwintyliard', 'kwintyliardy', 'kwintyliardów'],
        ['sekstylion', 'sekstyliony', 'sekstylionów'],
        ['sekstyliard', 'sekstyliardy', 'sekstyliardów'],
        ['septylion', 'septyliony', 'septylionów'],
        ['septyliard', 'septyliardy', 'septyliardów'],
        ['oktylion', 'oktyliony', 'oktylionów'],
        ['oktyliard', 'oktyliardy', 'oktyliardów'],
        ['nonilion', 'noniliony', 'nonilionów'],
        ['noniliard', 'noniliardy', 'noniliardów'],
        ['decylion', 'decyliony', 'decylionów'],
        ['decyliard', 'decyliardy', 'decyliardów']
    ]

    liczba = int(input('Podaj liczbę: '))

    wynik = ''
    w = 0

    while liczba > 0:

        s = math.floor(liczba % 1000 / 100)
        d = math.floor(liczba % 100 / 10)
        j = math.floor(liczba % 10)

        if d == 1 and j > 0:
            n = j
            d = 0
            j = 0
        else:
            n = 0

        if j == 1 and s+d+n == 0:
            f = 0
        elif j in range(2, 5):
            f = 1
        else:
            f = 2

        if s+d+n+j > 0:
            wynik = setki[s] + ' ' + dziesiatki[d] + ' ' + nascie[n] + jednosci[j] + ' '+ wielkosci[w][f] + ' ' + wynik

        w += 1
        liczba = math.floor(liczba/1000)

    return wynik




print (slownie())