with open("plik.txt", "r") as wczytanie:
    wczytaj = wczytanie.readlines()
    imiona = {}

    for imie in wczytaj:
        imie = imie.strip()
        if imie in imiona:
            imiona[imie] +=1
        else:
            imiona[imie] = 1
    print(imiona)