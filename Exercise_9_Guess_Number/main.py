import random

liczba = random.randint(0,9)

zgadywanka = int(input("Zgadnij liczbę! "))


while True:
    if zgadywanka>liczba:
        print("Podana liczba jest zbyt duża!!!")
        zgadywanka = int(input("Zgadnij ponownie! "))

    elif zgadywanka<liczba:
        print("Podana liczba jest za mała!!!")
        zgadywanka = int(input("Zgadnij ponownie! "))

    elif zgadywanka==liczba:
        print("Odgadłeś liczbę!!!")
        tak=input("Zagrać kolejny raz? T/N")
        if tak in ["N", "n"]:
            break
        if tak in ["t", "T"]:
            liczba = random.randint(0, 9)
            zgadywanka = int(input("Podaj liczbę! "))

