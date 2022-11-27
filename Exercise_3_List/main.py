# siema oto lista

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
lista2 = range(4,200)       # range tworzy listę od liczby 4 do 199

for element in lista:       # element oznacza wszystko w tabeli XD
    print(element)

for a in (lista):           # to wyrzuci tylko wartości z tabeli mniejsze niż 3
    if int(a)<<3:
        print(a, end = " ") # end = sprawi, że print nie będzie w nowej linii


print("")
ile = input("Ile liczb z listy wyświetlić?:" )

x = int(ile)
v = int(ile)

for b in (lista):
    if x>>0:
        print(b, end = " ")
        x=x-1
        print(x)

for c in (lista2):
    if v>>0:
        print(c, end = " ")
        v=v-1

# elif to jest inaczej elseif XD