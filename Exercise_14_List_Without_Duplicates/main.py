import random

lista1=[]
lista2=[]


def generacja_tabeli():
    a=40
    while a>0:
        lista1.append(random.randrange(0,20))
        a=a-1

def czyszczenie_duplikatow():
    for b in lista1:
        if b not in lista2:
            lista2.append(b)
            lista2.sort()

generacja_tabeli()
czyszczenie_duplikatow()

for element in lista1:
    print(element, end = ", ")

print("===============")

for element2 in lista2:
    print(element2, end = ", ")






