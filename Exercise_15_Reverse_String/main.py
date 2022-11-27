def liczenie():
    rozjazd = siema.split()   # rozjazd to inaczej lista składająca się z wyrazów w stringu. .split rozdziela wyrazy
    for element in rozjazd[::-1]:
        print(element)







siema = input("Podaj mi swoje zdanie: ")
liczenie()


