def stats_sword():
    print(weapon_sword.id,".Sword")
    print("DMG: ", weapon_sword.dmg_min, " - ", weapon_sword.dmg_max)
    print("Luck: ", weapon_sword.luck)
    print("Critical chance: ", weapon_sword.crit,"%")
    print("Attack speed: ", weapon_sword.attack_speed)
    print("Range: ",weapon_sword.range)
def stats_axe():
    print(weapon_axe.id,".Axe")
    print("DMG: ", weapon_axe.dmg_min, " - ", weapon_axe.dmg_max)
    print("Luck: ", weapon_axe.luck)
    print("Critical chance: ", weapon_axe.crit,"%")
    print("Attack speed: ", weapon_axe.attack_speed)
    print("Range: ",weapon_axe.range)
def stats_staff():
    print(weapon_staff.id,".Staff")
    print("DMG: ", weapon_staff.dmg_min, " - ", weapon_staff.dmg_max)
    print("Luck: ", weapon_staff.luck)
    print("Critical chance: ", weapon_staff.crit,"%")
    print("Attack speed: ", weapon_staff.attack_speed)
    print("Range: ",weapon_staff.range)

class sword:
    id = 1
    dmg_min = 1
    dmg_max = 5
    luck = 5
    crit = 2
    attack_speed = 2
    range = 2
class axe:
    id = 2
    dmg_min = 3
    dmg_max = 10
    luck = 0
    crit = 1
    attack_speed = 1
    range = 1
class staff:
    id = 3
    dmg_min = 1
    dmg_max = 4
    luck = 1
    crit = 1
    attack_speed = 2
    range = 7

weapon_sword = sword()
weapon_axe = axe()
weapon_staff = staff()

while True:
    print("1. Sword")
    print("2. Axe")
    print("3. Staff")
    weapon_choice = input("Select you weapon! ")
    print()
    match weapon_choice:
        case "1":
            stats_sword()
            print("You want to select sword?")
            confirmation = input("Y/N ")
            print()
            if confirmation.lower() == "y":
                print("Selected sword!")
                break
        case "2":
            stats_axe()
            print("You want to select axe?")
            confirmation = input("Y/N ")
            print()
            if confirmation.lower() == "y":
                print("Selected axe!")
                break
        case "3":
            stats_staff()
            confirmation = input("Y/N ")
            print()
            if confirmation.lower() == "y":
                print("Selected staff!")
                break


