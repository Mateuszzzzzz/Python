
rundy_string = input("Ile rund chcecie rozegrać? ")
rundy = max(1, int(rundy_string))
i = 1
gracz = "Pierwszego"
jeden = 0
dwa = 0

while i < rundy+1:
    print("Tura gracza pierwszego: ")
    ruch = input("Podaj swój ruch! Papier/Kamien/Nozyce")

    i = i+1

    print("Tura gracza drugiego: ")
    ruch2 = input("Podaj swój ruch! Papier/Kamien/Nozyce")

    if ruch in ["Papier", "papier", "PAPIER"] and ruch2 in ["Kamien", "kamien", "KAMIEN"]:
        print("Gracz pierwszy wygrywa!")
        jeden = jeden+1
    if ruch in ["Kamien", "kamien", "KAMIEN"] and ruch2 in ["Nozyce", "nozyce", "NOZYCE"]:
        print("Gracz pierwszy wygrywa!")
        jeden = jeden+1
    if ruch in ["Nozyce", "nozyce", "NOZYCE"] and ruch2 in ["Papier", "papier", "PAPIER"]:
        print("Gracz pierwszy wygrywa!")
        jeden = jeden+1

    if ruch2 in ["Papier", "papier", "PAPIER"] and ruch in ["Kamien", "kamien", "KAMIEN"]:
        print("Gracz drugi wygrywa!")
        dwa = dwa+1
    if ruch2 in ["Kamien", "kamien", "KAMIEN"] and ruch in ["Nozyce", "nozyce", "NOZYCE"]:
        print("Gracz drugi wygrywa!")
        dwa = dwa+1
    if ruch2 in ["Nozyce", "nozyce", "NOZYCE"] and ruch in ["Papier", "papier", "PAPIER"]:
        print("Gracz drugi wygrywa!")
        dwa = dwa+1
    else:
        print("Remis!")





print("Wynik to: ")
print("Gracz pierwszy: ", jeden)
print("Gracz drugi: ", dwa)
if jeden>dwa:
    print("Gracz pierwszy jest zwycięzcą!")
elif jeden<dwa:
    print("Gracz drugi jest zwycięzcą!")
else:
    print("Remis!")
