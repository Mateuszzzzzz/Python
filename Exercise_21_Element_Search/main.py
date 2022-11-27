import random

def generacja_listy():
    dlugosc = int(input("Podaj długość listy: "))
    rozmiar = int(input("Podaj maksymalną liczbę na liście: "))
    lista = [random.randint(0,rozmiar) for i in range(dlugosc)]
    lista.sort()
    print(lista)
    ile = len(lista)
    ile2 = ile+1
    min = 1
    max = ile
    srednia = (min + max) / 2
    s = input("Podaj szukaną liczbę: ")
    p = int(s)
    srednia2=int(srednia)

    while min<=max:
        if p > lista[srednia2]:
            srednia2 = srednia2 + 1
            ile2 = ile2 - 1
            if ile2 > 0:
                continue
            else:
                print("Liczba nie znajduje się na liście!")
                break

        if p<lista[srednia2]:
            srednia2 = srednia2-1
            ile2 = ile2 - 1
            if ile2>0:
                continue
            else:
                print("Liczba nie znajduje się na liście!")
                break

        if p==lista[srednia2]:
            print("Liczba",p,"znajduje się na liście!")
            return False
        else:
            print("Liczba nie znajduje się na liście!")
            break

    if min>max:
        print("Liczba nie znajduje się na liście!")



generacja_listy()

