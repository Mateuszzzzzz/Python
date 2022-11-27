ile=int(input("Ile liczb ciągu Fibonacciego wyświetlić? "))

pierwszy=1
drugi=1
if ile>2:
    print(pierwszy)
    print(drugi)
    ile2=ile-2
    while ile2 > 0:
        ile2=ile2-1
        trzeci = pierwszy+drugi
        print(trzeci)
        pierwszy = drugi
        drugi = trzeci
elif ile==2:
    print(pierwszy)
    print(drugi)
elif ile==1:
    print(pierwszy)

