'''
Laboratorium 9
Agnieszka Lempaszek
moduł słowa
'''

def czy_palindrom(word):
    '''
    Funkcja pobiera na wejściu string, i zwraca informację czy jest to palindrom
    '''
    if type(word) is str:
        if str(word.lower()) == str(word.lower())[::-1]:
            return "Słowo jest palindromem"
        else:
            return "Słowo NIE jest palindromem"
    else:
        return "Podaj string"



def czy_rowne(words):
    '''
    Funkcja pobiera na wejściu słowa w formie listy lub string i sprawdza czy ich długość jest równa
    '''
    newArray = []
    if type(words) is str:
        wordsArray = words.split()
    elif type(words) is list:
        wordsArray = words
    else:
        return "Podaj słowa w postaci listy lub string"

    newArray.append(wordsArray[0])
    for i in range(1, (len(wordsArray))):
        if (len(wordsArray[i])) == len(wordsArray[0]):
            newArray.append(wordsArray[i])
    if len(newArray) == len(wordsArray):
        return "Podane słowa są równe"
    else:
        return "Podane słowa nie są równej długości"