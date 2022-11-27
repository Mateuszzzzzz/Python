jeden = int(input("Podaj licznik: "))
dwa = int(input("Podaj mianownik: "))
trzy = 0

def czy_sie_dziela():
    if dwa>jeden:
        if dwa%jeden==0:
            trzy = dwa/jeden
            print("1 /",trzy)
        elif jeden%dwa==0:
            trzy = jeden/dwa
            print("Liczby dzielą się na siebie. Wynik to: ",trzy)
    elif jeden>dwa and jeden%dwa==0:
        print(jeden/dwa)

def czy_parzyste():
    jeden_dwa=jeden
    dwa_dwa=dwa
    while jeden%2==0 and dwa%2==0:

        jeden_dwa=jeden_dwa/2
        dwa_dwa=dwa_dwa/2
        if jeden_dwa%2!=0 or dwa_dwa%2!=0:

            if jeden_dwa%3==0 and dwa_dwa%3==0:
                jeden_cztery=jeden_dwa
                dwa_cztery=dwa_dwa
                while jeden_dwa%3==0 and dwa_dwa%3==0:
                    jeden_cztery = jeden_cztery/3
                    dwa_cztery= dwa_cztery/3
                    if dwa_cztery%5==0 or jeden_cztery%5==0:
                        jeden_piec=jeden_cztery
                        dwa_piec=dwa_cztery
                        while jeden_piec%5==0 and dwa_piec%5==0:
                            jeden_piec=jeden_piec/5
                            dwa_piec=dwa_piec/5
                            if jeden_piec%5!=0 or dwa_piec%5!=0:
                                print(jeden_piec, dwa_piec)
                    else:
                        print(jeden_cztery, "/", dwa_cztery)
                        break
                break
            else:
                print(jeden_dwa, "/", dwa_dwa)
            break

def czy_nieparzyste_3():
    jeden_trzy=jeden
    dwa_trzy=dwa
    while jeden%3==0 and dwa%3==0:
        jeden_trzy=jeden_trzy/3
        dwa_trzy=dwa_trzy/3
        if jeden_trzy%3!=0 or dwa_trzy%3!=0:

            if jeden_trzy%2==0 and dwa_trzy%2==0:
                jeden_piec=jeden_trzy
                dwa_piec=dwa_trzy
                while jeden_trzy%2==0 and dwa_trzy%2==0:
                    jeden_piec=jeden_piec/2
                    dwa_piec=dwa_piec/2
                    if jeden_piec%5==0 or dwa_piec%5==0:
                        jeden_szesc = jeden_piec
                        dwa_szesc = dwa_piec
                        while jeden_szesc % 5 == 0 and dwa_szesc % 5 == 0:
                            jeden_szesc = jeden_szesc / 5
                            dwa_szesc = dwa_szesc / 5
                            if jeden_szesc % 5 != 0 or dwa_szesc % 5 != 0:
                                print(jeden_szesc, "/", dwa_szesc)


                    else:
                        print(jeden_piec, "/", dwa_piec)
                        break
                break
            else:
                print(jeden_trzy, "/", dwa_trzy)
            break


def czy_nieparzyste_5():
    jeden_szesc = jeden
    dwa_szesc = dwa
    while jeden%5==0 and dwa%5==0:
        jeden_szesc=jeden_szesc/5
        dwa_szesc=dwa_szesc/5
        if jeden_szesc%5!=0 or dwa_szesc%5!=0:
            print(jeden_szesc, "/", dwa_szesc)
            break

def przyblizenie():
    print("Wynik w przybliżeniu to: ", jeden/dwa)

czy_sie_dziela()
czy_parzyste()
czy_nieparzyste_3()
czy_nieparzyste_5()
przyblizenie()
print("Jeżeli przybliżenie to jedyny wyświetlony wynik, to znaczy, że liczba się nie skraca wcale")