items = []
how_many_items = 0

def list_of_items():
    for element in items:
        print (element)

def create_item():
    global how_many_items
    item_to_be_added = ("ID: ")
    id = how_many_items + 1
    id = str(id)
    how_many_items += 1
    item_to_be_added+=id

    print("Write your item's name:")
    name = input()
    item_to_be_added += " Name: "
    item_to_be_added += name

    print("Write your item's description:")
    description = input()
    print("Your item is:")
    print(id,".", name)
    print(description)
    print()
    item_to_be_added += " Description: "
    item_to_be_added += description
    item_to_be_added += ""
    items.append(item_to_be_added)
    return(items)

def remove_items():
    print("Please write ID of an item that you want to remove:")
    which_to_remove = int(input())
    if which_to_remove<=how_many_items:
        del items[which_to_remove-1]
    else:
        print("There are no items which this ID!")


while True:
    print("1. Create your own item")
    print("2. List of items")
    print("3. Remove items")
    print("4. Exit")

    i = int(input())

    if i == 1:
        create_item()
    elif i == 2:
        list_of_items()
    elif i == 3:
        remove_items()
    else:
        break