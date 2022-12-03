email = input("Please, write down your email! ")

def check(mail):
    if str("@") in mail:
        print("Tak")
        return True

def split(word):
    first_part=[]
    first_part_str=""
    for element in word:
        if element!="@":
            first_part.append(element)
        else:
            break

    for element2 in first_part:
        first_part_str += element2
    print(first_part_str)
    return first_part_str


def split2(word, email2):
    email2 = email2.replace(word,'')
    email2 = email2.replace('@', '')
    print(email2)


if check(email):
    p1 = split(email)
    split2(p1, email)