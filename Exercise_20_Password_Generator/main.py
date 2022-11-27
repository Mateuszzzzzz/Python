import random

Jakie = input("Jakie to ma być hasło? Silne/Średnie/Słabe?")
wybor = ("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-=!@#$%^&*()[];':")
haslo = ""

if Jakie=="Silne":
    i = 10
    while i >0:
        haslo +=random.choice(wybor)
        i = i-1
        if i == 0:
            print(haslo)
            i = -1
if Jakie=="Średnie":
    i = 7
    while i > 0:
        haslo += random.choice(wybor)
        i = i-1
        if i == 0:
            print(haslo)
            i = -1

if Jakie=="Słabe":
    i = 5
    while i >0:
        haslo +=random.choice(wybor)
        i = i-1
        if i == 0:
            print(haslo)
            i = -1




