"Laboratorium 2, Agnieszka Lempaszek"

import math
#------------------------------------------------------------------------------
print('\nZadanie 2.1\n')

a, b, c = 1, -12, 35
# ma działać dla dowolnych a, b, c, dla których istnieją rozwiązania

delta = (b ** 2) - (4*a*c)          # zastąp zero wzorem na deltę
x_1 = (-b - math.sqrt(delta))/(2*a)           # zastąp zero wzorem na rozwiązanie nr 1
x_2 = (-b + math.sqrt(delta))/(2*a)          # zastąp zero wzorem na rozwiązanie nr 2  

# Wypisz równanie

print('\nRównanie',a,'x^2 + ',b,'x + ',c,' = 0')

# Wypisz rozwiązania

print('\nRozwiązania: x_1 =',x_1,' x_2 =',x_2)

#------------------------------------------------------------------------------
print('\nZadanie 2.2\n')

l = input("Podaj liczbę:")			# zastąp odpowiednią funkcją
li = int(l)

# Wypisz wprowadzoną liczbę

print(l)

# Wypisz podwojoną

print('Twoja liczba po podwojeniu to', li*2)

# Wypisz wiele razy


print('Powtarzając twoją liczbę 5 razy otrzymamy:',l*5)

# Wypisz podzieloną przez 3


print('Podzielona przez 3:',li/3.0)

# Wypisz resztę z dzielenia

print('Reszta z dzielenia przez 7 to: ', li % 7, '\n')

#------------------------------------------------------------------------------
