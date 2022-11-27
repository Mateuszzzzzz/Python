tekst = input("Hello, please type word:")


if tekst.isnumeric():
    print("It's not a word!")

else:
    if tekst==tekst[::-1]:          #sprawdza czy string od tyłu jest tak samo
        print("It word spells same backwards!")
    else:
        print("It word doesn't spells same backwards!")

