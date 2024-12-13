import codecs
from threading import Timer

def tekst(plik):
    with codecs.open(plik, "r", 'utf-8') as tekst:
        return tekst.readlines()

def wybor_tekstu(numer):
    wiadomosc_bledu = "Podano zły numer tekstu."
    if(numer == 1):
        with codecs.open("Pisanie_zaklec/Zaklecia1.txt", 'r', 'utf-8') as plik:
            return formatowanie(plik.readlines())
    elif(numer == 2):
        with codecs.open("Pisanie_zaklec/Zaklecia2.txt", 'r', 'utf-8') as plik:
            return formatowanie(plik.readlines())
    elif(numer == 3):
        with codecs.open("Pisanie_zaklec/Zaklecia3.txt", 'r', 'utf-8') as plik:
            return formatowanie(plik.readlines())
    else:
        return wiadomosc_bledu

def formatowanie(lista):
    wyrazy_temp = []
    wyrazy = []
    for wartosc in lista:
        wyrazy_temp.append(wartosc.split())
    for a in wyrazy_temp:
        wyrazy.extend(a)
    return wyrazy

def przechwytywanie(wybrana_dlugosc_programu):
    t = Timer(wybrana_dlugosc_programu, lambda: print("\nCzas minął.\nWciśnij ENTER, aby zobaczyć wyiki."))            #t jest obiektem threading.Timer gdzie Timer(x, y) po upływie czasu x wywoła funkcję y
    t.start()                                                                       #zainicjowanie nowego procesu
    print("\nMasz", str(wybrana_dlugosc_programu), "sekund na napisanie tekstu\n")  
    odpowiedz = input()
    t.cancel()                                                                      #zatrzymanie procesu i wykonanie funkcji lambda: y
    odpowiedz + ".STOP!#"                                                           #dodaję na końcu ".STOP!#", żeby wiedzieć w którym momencie użytkownik skończył pisać
    return odpowiedz.split()

# zamiast funkcji lambda: print("\nCzas minął")
# def czas_minal():
#     print("\nCzas minął")

def sprawdzanie_poprawnosci(wzorzec, przepisane):
    i = 0
    liczba_poprawnych = 0
    for i in range(len(przepisane)):
        if(przepisane[i] == wzorzec[i]):
            liczba_poprawnych += 1
        elif(przepisane[i] == '.STOP!#'):
            return liczba_poprawnych
        i += 1
    return liczba_poprawnych

def main():
    while True:
        print("Witamy w sprawdzaniu szybkości pisania. wybierz tekst, w którym chcesz się sprawdzić: \n")
        print("1. Fiku-Miku")
        print("2. Monolog skryby")
        print("3. Lorem Ipsum")
        print("4. Wyjście z programu")
        wybor = int(input())
        if(wybor == 4):
            exit()
        try:
            sekundy = int(input("Wybierz czas pisania spośród podanych (30, 60, 90 [sek.]): "))
            if(sekundy != 30 and sekundy != 60 and sekundy != 90):
                print("Wybrano złą opcję.")
                continue
        except:
            print("Zły format czasu. ")
        tekst = wybor_tekstu(wybor)
        print(tekst)
        przepisany_tekst = przechwytywanie(sekundy)
        ilosc_poprawnych = sprawdzanie_poprawnosci(tekst, przepisany_tekst)
        print(f"Liczba poprawnie przepisanych słów: {ilosc_poprawnych}, stanowi to {round(ilosc_poprawnych/len(tekst), 2)} długości całego tekstu!")
        print(f"Prędkość pisania wynosi {ilosc_poprawnych/(sekundy/60)} słów na minutę.\n")


if __name__ == '__main__':
    main()
