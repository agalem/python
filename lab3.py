"Laboratorium 3, Agnieszka Lempaszek"

import math

#------------------------------------------------------------------------------
print('\nZadanie 3.1\n')

a, b, c = 1, -4, 3
# ma działać dla dowolnych a, b, c

delta = (b ** 2) - (4*a*c)          # zastąp zero wzorem na deltę

# Wypisz równanie

print('\nRównanie ',a,'x^2 + ',b,'x + ',c,' = 0')

# Wypisz rozwiązania

if(delta > 0):
    print ('Rozwiązania: x_1 = ',(-b - math.sqrt(delta))/(2*a),' x_2 = ',(-b + math.sqrt(delta))/(2*a))
elif(delta==0):
    print ('Rozwiązanie: x_1 = x_2 = ',-b/(2*a))
else:
    print ('Rozwiązanie: brak')


#------------------------------------------------------------------------------
print('\nZadanie 3.2\n')

n, p = 60, 37
# ma działać dla dowolnych n i p

# Wypisz dzielniki n

print ('Dzielniki liczby ',n,': ',[x for x in range(1, n+1) if n%x == 0])

# Wypisz dzielniki p

print ('Dzielniki liczby ',p,': ',[x for x in range(1, p+1) if p%x == 0])

#------------------------------------------------------------------------------
print('\nZadanie 3.3\n')

limit = 100
numbers = range(1, limit+1)

# Zastąp pustą listę wyrażeniem zwracającym liczby pierwsze z zakresu od 1 do 'limit'
primes = [x for x in numbers if x != 1 if all(x % y != 0 for y in range(2, x))]

print('Liczby pierwsze od 1 do %d: %s' % (limit, primes))