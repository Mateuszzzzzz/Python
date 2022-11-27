Liczba = input("Podaj liczbę: ")
if Liczba.isnumeric():
    if int(Liczba)%2==0:  #co oznacz %? np 7%2 = 3 i 1 reszty. wynik = 1. 8%2 = 4, wynik = 0
        print("Liczba jest parzysta!!")
    else:
        print("Liczba nie jest parzysta??????")
else:
    print("Mordo to nie jest liczba")



