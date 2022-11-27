import random

Lista1_1 = random.randrange(1,10)
Lista1_2 = random.randrange(10,20)

Lista2_1 = random.randrange(10,25)
Lista2_2 = random.randrange(25,40)



Lista1 = range(Lista1_1, Lista1_2)
Lista2 = range(Lista2_1, Lista2_2)


print("Liczby z tabeli 1:", end=" ")
for a in Lista1:
    print(a, end=" ")
print()

print("Liczby z tabeli 2:", end=" ")
for b in Lista2:
    print(b, end=" ")
print()

print("Wspólne liczby:", end=" ")
for c in Lista2:
    if c in Lista1:
        print(c, end=" ")