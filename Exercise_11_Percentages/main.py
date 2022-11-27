print("1. Znamy 100%, szukamy wartości konkretnego procentu")
print("2. Znamy ileś procent, szukamy 100% po jednej obiżce/podwyżce")
print("3. Znamy wartość podstawową oraz wartość po podwyżce/obniżce. Szukamy o ile procent nastąpiła zmiana.")

jaki_przypadek = int(input("Wybierz rodzaj problemu:"))

def przypadek1():
    sto_pro = int(input("Podaj 100%: "))
    szukany_pro = int(input("Podaj szukany %: "))
    wynik = sto_pro * szukany_pro / 100
    print(szukany_pro, "% z ", sto_pro, " jest równe: ", wynik)

def przypadek2():
    ile_znamy = int(input("Podaj jaki procent znamy: "))
    wartosc_ile = int(input("Podaj wartość tego procenta: "))
    wartosc_jeden = wartosc_ile/ile_znamy
    wyniczek = wartosc_jeden*100
    print("100% dla tej wartości to: ",wyniczek)

def przypadek3():
    znane = int(input("Podaj podstawową wartość: "))
    zmienione = int(input("Podaj wartość po zmianie: "))
    if znane>zmienione:
        zmiana = znane-zmienione
        jeden_p = znane/100
        wynik = 0
        ile=jeden_p
        while zmiana>=jeden_p:
            wynik=wynik+1
            ile = ile+jeden_p
            if ile>zmiana:
                break
        print("Spadek wartości o: ",wynik,"%")

    if znane<zmienione:
        zmiana = zmienione-znane
        jeden_p=znane/100
        wynik = 0
        ile = jeden_p
        while zmiana>=jeden_p:
            wynik=wynik+1
            ile = ile+jeden_p
            if ile>zmiana:
                break
        print("Wzrost wartości o: ", wynik,"%")

    if znane==zmienione:
        print("Nie ma żadnej zmiany!")

if jaki_przypadek==1:
    przypadek1()

if jaki_przypadek==2:
    przypadek2()

if jaki_przypadek==3:
    przypadek3()

