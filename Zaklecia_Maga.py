import codecs
import os
from threading import Timer

def tekst(plik):
    with codecs.open(plik, "r", 'utf-8') as file:
        return file.readlines()
  
def wybor_tekstu(numer):
    return_val = "Podano zły numer tekstu."
    if numer == 1:
        with codecs.open("Zaklecia/1.txt", 'r', 'utf-8') as plik:
            return formatowanie(plik.readlines())
    elif numer == 2:
        with codecs.open("Zaklecia/2.txt", 'r', 'utf-8') as plik:
            return formatowanie(plik.readlines())
    elif numer == 3:
        with codecs.open("Zaklecia/3.txt", 'r', 'utf-8') as plik:
            return formatowanie(plik.readlines())
    else:
        return return_val

# Dunno what this function is to do about
def formatowanie(lista):
    wyrazy_temp = []
    wyrazy = []
    for wartosc in lista:
        wyrazy_temp.append(wartosc.split())
    for a in wyrazy_temp:
        wyrazy.extend(a)
    return ' '.join(wyrazy)

def przechwytywanie(wybrana_dlugosc_programu):
    t = Timer(wybrana_dlugosc_programu, lambda: print("\nCzas minął. "))            #Muszę jeszcze przeanalizować jak to działa, ale wygląda obiecująco
    t.start()
    print("\nMasz", str(wybrana_dlugosc_programu), "sekund na napisanie tekstu\n")
    odpowiedz = input()
    t.cancel()
    return odpowiedz.split()

def sprawdzanie_poprawnosci(wzorzec, przepisane):
    i = 0
    liczba_poprawnych = 0
    for i in range(len(przepisane)):
        if(przepisane[i] == wzorzec[i]):
            liczba_poprawnych += 1
        i += 1
    return liczba_poprawnych

def main():
    while True:
        print("Witamy w sprawdzaniu szybkości pisania. wybierz tekst, w którym chcesz się sprawdzić: \n")
        print("1. Monolog maga")
        print("2. Monolog skryby")
        print("3. Lorem ipsum")
        print("4. Wyjscie z programu")
        wybor = int(input())
        if wybor == 4:
            exit()
        try:
            sekundy = int(input("Wybierz czas pisania spośród podanych (30, 60, 90 [sek.]): "))
            if sekundy != 30 and sekundy != 60 and sekundy != 90:
                print("Wybrano złą opcję.")
                continue
        except:
            print("Zły format czasu. ")
        tekst = wybor_tekstu(wybor)
        print(tekst)
        przepisany_tekst = przechwytywanie(sekundy)
        ilosc_poprawnych = sprawdzanie_poprawnosci(tekst, przepisany_tekst)
        print(f"Ilość poprawnie przepisanych słów: {ilosc_poprawnych}, stanowi to {round(ilosc_poprawnych/len(tekst), 2)} długości całego tekstu!\n")
        print(f"Prędkość pisania wynosi {ilosc_poprawnych/(sekundy/60)} słów na minutę.")


if __name__ == '__main__':
    main()
