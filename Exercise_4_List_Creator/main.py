# kreator listy

jeden = input("Podaj pierwszą cyfrę: ")
dwa = input("Podaj ostatnią cyfrę: ")
trzy = input("Podaj ile liczb z listy wyświetlić: ")


n =int(jeden)

def dzielnik():
    dzielnik_2 = 1
    while dzielnik_2<=dwa_liczba:
        if n%dzielnik_2==0 and dzielnik_2<=n:
            print(max(1,dzielnik_2), end =" ")


            dzielnik_2=dzielnik_2+1


        elif n%dzielnik_2!=0:
            dzielnik_2 = dzielnik_2 + 1

        continue

if jeden.isnumeric():
    jeden_liczba = int(jeden)

    if dwa.isnumeric():
        dwa_liczba = int(dwa)+1             # plus jeden aby zasięg był do podanej liczby włącznie, a nie kończył się przed nią

        if trzy.isnumeric() and dwa_liczba>=jeden_liczba:
            trzy_liczba = int(trzy)
            lista3 = range(jeden_liczba, dwa_liczba)


            if trzy_liczba>>0 and trzy_liczba<=dwa_liczba-jeden_liczba:
                    m = int(trzy)

                    for trzy_liczba in (lista3):
                        if m>>1:

                            print(n,"Jej dzielniki to:", end = " ")
                            dzielnik()
                            n=n+1
                            m=m-1
                            print()

                        if m==1:

                            print(n,"Jej dzielniki to:", end = " ")
                            dzielnik()
                            n = n + 1
                            m=m-1
                            print()


            elif trzy_liczba==0 and trzy_liczba<=dwa_liczba:
                    print("Koniec wyników!")

            else:
                    print("Błąd!")
        else:
            print("Błąd!")
    else:
        print("Nieprawidłowa druga liczba!")
else:
    print("Nieprawidłowa pierwsza liczba!")
