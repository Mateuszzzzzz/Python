import random

liczba=[]
k=0
def generacja_liczby():
    a = int(random.randrange(0,10))
    liczba.append(a)
    b = int(random.randrange(0,10))
    if b!=a:
        liczba.append(b)
    else:
        while b==a:
            b = int(random.randrange(0, 10))
            if b!=a:
                liczba.append(b)
                break
    c = int(random.randrange(0,10))
    if c!=a and c!=b:
        liczba.append(c)
    else:
        while c==a or c==b:
            c = int(random.randrange(0, 10))
            if c!=a and c!=b:
                liczba.append(c)
                break

    d = int(random.randrange(0,10))
    if d!=a and d!=b and d!=c:
        liczba.append(d)
    else:
        while d == a or d == b or d==c:
            d = int(random.randrange(0,10))
            if d!= b and d!= a and d!=c:
                liczba.append(d)
                break

    for element in liczba:
        print(element, end="")
    print()


def zgadywanie():
    cow = 0
    bull = 0
    while cow!=4:
        if cow>0:
            cow=0
        if bull>0:
            bull=0
        zgadywanka = input("Podaj liczbę: ")
        n=0
        proby = 1
        while n<4:
            a = int(zgadywanka[n])
            b = int(liczba[n])
            c = str(liczba)
            d = str(a)



            if a==b:
                cow = cow+1
                if cow == 4:
                    print("Wygrałeś!")
                    print("Zajęło Ci to", proby, "prób!")
                    break

            elif d in c and a!=b:
                uzyte = int(d)
                bull = bull+1

            n += 1

            if cow!=4 and n==4:
                print("Jest", cow, "krów i", bull, "byków!")
                proby += 1
                continue





if __name__ == "__main__":
    generacja_liczby()
    zgadywanie()
