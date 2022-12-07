def acronym(name):
    acro = []

    for i in range(1, len(name)):
        if name[i]==" ":
            acro+=name[i+1]
        i+=1
    acro_str="".join(acro)
    return acro_str.upper()


print("We will create acronym from given words!")
name = input("Please input your name or perhaps your company name: ")
print(name[0].upper(), end="")
print(acronym(name))