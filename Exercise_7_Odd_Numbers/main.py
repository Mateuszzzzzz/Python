import random

a=0
lista = []

dlugi = input("Jak wiele liczb wygenerować?: ")

if dlugi.isnumeric():
    dlugi2 = int(dlugi)
else:
    dlugi2 = 40

while a < dlugi2:
    while True:                         # Tutaj while True oznacza, że się zapętla bez końca.
        b=random.randrange(0,max(1000,dlugi2*20))
        if b not in lista:              # ten warunek sprawdza czy tej liczby nie ma. Jeśli nie ma to kończy losowanie.
            break
    lista.append(b)                     # .append() dodaje do listy jedną rzecz, tę z nawiasu
    a = a+1

lista.sort()                            # .sort() sortuje listę od najmniejszych do największych
print(lista)

print("Nieparzyste elementy listy: ")
for nieparzyste in lista:
    if nieparzyste%2!=0:
        print(nieparzyste, end=", ")