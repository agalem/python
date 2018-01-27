# -*- coding: utf-8 -*-

'''
Agnieszka Lempaszek
laboratorium 10
'''

class Osoba:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def introduce(self):
        print ('Nazywam się %s %s i mam %d lat' % (self.name, self.surname, self.age))

class Student(Osoba):
    oceny = []
    czy_stypendium = None

    def dodaj_ocene(self, oceny):
        self.oceny.append(oceny)
        print ('Moje oceny to: %s' % (self.oceny))

    def pokaz_oceny(self):
        print ('Moje oceny to: %s' % (self.oceny))

    def usun_oceny(self):
        self.oceny = []
        print ('Usunięto oceny: %s' % (self.oceny))

    def stypendium(self):
        if(self.czy_stypendium != None):
            print ('Student posiada stypendium')
        else:
            print ('Student nie posiada stypendium')

    def dodaj_stypendium(self):
        self.czy_stypendium = True
        print ('Dodano stypendium')

    def usun_stypendium(self):
        self.czy_stypendium = None
        print ('Usunieto stypendium')


class Wykladowca(Osoba):
    stanowisko = 'Profesor UJ'
    pensja = 0
    urlop = 30

    def pokaz_stanowisko(self):
        print ('Stanowisko: %s' % (self.stanowisko))

    def zmien_stanowisko(self, nowe_stanowisko):
        self.stanowisko = nowe_stanowisko
        print ('Zmieniono stanowisko na %s' % (self.stanowisko))

    def pokaz_pensje(self):
        print ('Aktualna pensja wynosi: %s' % (self.pensja))

    def podwyzka(self, kwota):
        self.pensja += kwota
        print ('Aktualna pensja wynosi: %s' % (self.pensja))

    def obnizka(self, kwota):
        self.pensja -= kwota
        print ('Aktualna pensja wynosi: %s' % (self.pensja))

    def pokaz_urlop(self):
        print ('Pozostało %s dni urlopu' % (self.urlop))

    def zmniejsz_urlop(self, dni):
        self.urlop -= dni
        print ('Pozostało %s dni urlopu' % (self.urlop))

    def zwieksz_urlop(self, dni):
        self.urlop += dni
        print ('Pozostało %s dni urlopu' % (self.urlop))


x = Osoba('Marek', 'Kowalski', 44)

y = Student('Justyna', 'Kowalczyk', 23)

z = Wykladowca('Jan', 'Matejko', 56)