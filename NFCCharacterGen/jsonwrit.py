import json

datafields = {
    "C": f"{'x' * 12}",  # CODENAME
    "N": f"{'x' * 28}",  # NAME
    "T": f"{'x' * 1}",  # TYPE
    "U": {  # UTILITIES
        "H": f"{'x' * 12}",  # HEAD
        "E": f"{'x' * 12}",  # EYES
        "F": f"{'x' * 12}",  # FACE
        "O": f"{'x' * 12}",  # OUTERWEAR
        "I": f"{'x' * 12}",  # INNERWEAR
        "L": f"{'x' * 12}",  # LOWERWEAR
        "G": f"{'x' * 12}",  # GLOVES
        "S": f"{'x' * 12}",  # SHOES
    },
    "H": {  # MAIN
        "N": f"{'x' * 10}",  # NAME
        "A": 100,  # ATTACK POWER
        "T": f"{'x' * 1}",  # TYPE
        "R": 100,  # RATE OF ATTACK
        "L": 100,  # RELOAD TIME
        "C": 100  # CAPACITY
    },
    "L": {  # SUB
        "N": f"{'x' * 10}",  # NAME
        "A": 100,  # ATTACK POWER
        "T": f"{'x' * 1}",  # TYPE
        "R": 100,  # RATE OF ATTACK
        "L": 100,  # RELOAD TIME
        "C": 100  # CAPACITY
    },
    "S": {  # BASE STATS
        "H": 1000,  # MAIN HEALTH
        "S": 1000,  # REGENERATING SHIELD
        "M": 1000,  # HOST HP AFTER DETACH
        "J": 100,  # SHIELD RECHARGE RATE
        "O": 100,  # ABILITY TO OVERTAKE HOST AFTER DETACH
        "A": 100,  # BASE ATTACK
        "D": 100,  # BASE DEFENSE
        "Q": 100,  # BASE SPEED
        "I": 100,  # BASE INTELLIGENCE
        "E": 100,  # BASE ENDURANCE
        "P": 100,  # BASE STRENGTH
        "W": 100,  # BASE LUCK
        "G": 100  # BASE FIREARMS HANDLING
    }
}


def characteristics():
    for key, value in {"C": ["CODENAME", 12], "N": ["NAME", 28], "T": ["TYPE", 1]}.items():
        temp = f"{'c'*100}"
        while len(temp) > value[1]:
            temp = str(input(f"INPUT CHARACTER {value[0]} (CHARACTER LIMIT {value[1]}): "))
        datafields[key] = temp
    write_step()


def utilities():
    for key, value in datafields["U"].items():
        temp = f"{'c' * 100}"
        if key == "H":
            while len(temp) > 12:
                temp = str(input("INPUT CHARACTER HEADGEAR (MAX 12 CHARACTERS): "))
            datafields["U"][key] = temp
        elif key == "E":
            while len(temp) > 12:
                temp = str(input("INPUT CHARACTER EYEWEAR (MAX 12 CHARACTERS): "))
            datafields["U"][key] = temp
        elif key == "F":
            while len(temp) > 12:
                temp = str(input("INPUT CHARACTER FACEWEAR (MAX 12 CHARACTERS): "))
            datafields["U"][key] = temp
        elif key == "O":
            while len(temp) > 12:
                temp = str(input("INPUT CHARACTER OUTERWEAR (MAX 12 CHARACTERS): "))
            datafields["U"][key] = temp
        elif key == "I":
            while len(temp) > 12:
                temp = str(input("INPUT CHARACTER INNERWEAR (MAX 12 CHARACTERS): "))
            datafields["U"][key] = temp
        elif key == "L":
            while len(temp) > 12:
                temp = str(input("INPUT CHARACTER LOWERWEAR (MAX 12 CHARACTERS): "))
            datafields["U"][key] = temp
        elif key == "G":
            while len(temp) > 12:
                temp = str(input("INPUT CHARACTER HANDWEAR (MAX 12 CHARACTERS): "))
            datafields["U"][key] = temp
        elif key == "S":
            while len(temp) > 12:
                temp = str(input("INPUT CHARACTER FOOTWEAR (MAX 12 CHARACTERS): "))
            datafields["U"][key] = temp
        else:
            break
    write_step()


def weapon_main():
    for key, value in datafields["H"].items():
        temp = 10000
        if key == "N":
            temp = f"{'x' * 100}"
            while len(temp) > 10:
                temp = str(strip_specials(input("INPUT PRIMARY WEAPON NAME (MAX 10 CHARACTERS, SPECIALS WILL BE STRIPPED): ")))
            datafields["H"][key] = temp
        elif key == "A":
            while temp > 999:
                temp = int(input("INPUT PRIMARY WEAPON ATTACK POWER (LIMIT 999): "))
            datafields["H"][key] = temp
        elif key == "T":
            temp = f"{'x' * 100}"
            while len(temp) > 1:
                temp = str(type_check(strip_specials(input("INPUT PRIMARY WEAPON TYPE (MAX 1 CHARACTERS, SPECIALS WILL BE STRIPPED): "))))
            datafields["H"][key] = temp
        elif key == "R":
            while temp > 999:
                temp = int(input("INPUT PRIMARY WEAPON RATE OF ATTACK (LIMIT 999): "))
            datafields["H"][key] = temp
        elif key == "L":
            while temp > 999:
                temp = int(input("INPUT PRIMARY WEAPON RELOAD RATE (LIMIT 999): "))
            datafields["H"][key] = temp
        elif key == "C":
            while temp > 999:
                temp = int(input("INPUT PRIMARY WEAPON AMMO CAPACITY (LIMIT 999): "))
            datafields["H"][key] = temp
        else:
            break
    write_step()


def weapon_secondary():
    for key, value in datafields["L"].items():
        temp = 10000
        if key == "N":
            temp = f"{'x' * 100}"
            while len(temp) > 10:
                temp = str(
                    strip_specials(input("INPUT PRIMARY WEAPON NAME (MAX 10 CHARACTERS, SPECIALS WILL BE STRIPPED): ")))
            datafields["L"][key] = temp
        elif key == "A":
            while temp > 999:
                temp = int(input("INPUT PRIMARY WEAPON ATTACK POWER (LIMIT 999): "))
            datafields["L"][key] = temp
        elif key == "T":
            temp = f"{'x' * 100}"
            while len(temp) > 1:
                temp = str(type_check(
                    strip_specials(input("INPUT PRIMARY WEAPON TYPE (MAX 1 CHARACTERS, SPECIALS WILL BE STRIPPED): "))))
            datafields["L"][key] = temp
        elif key == "R":
            while temp > 999:
                temp = int(input("INPUT PRIMARY WEAPON RATE OF ATTACK (LIMIT 999): "))
            datafields["L"][key] = temp
        elif key == "L":
            while temp > 999:
                temp = int(input("INPUT PRIMARY WEAPON RELOAD RATE (LIMIT 999): "))
            datafields["L"][key] = temp
        elif key == "C":
            while temp > 999:
                temp = int(input("INPUT PRIMARY WEAPON AMMO CAPACITY (LIMIT 999): "))
            datafields["L"][key] = temp
        else:
            break
    write_step()


def character_stats():
    for key, value in datafields["S"].items():
        temp = 10000
        if key == "H":
            while temp > 9999:
                temp = int(input("INPUT CHARACTER BASE HEALTH (MAX 9999): "))
            datafields["S"][key] = temp
        elif key == "S":
            while temp > 9999:
                temp = int(input("INPUT CHARACTER BASE SHIELD (MAX 9999): "))
            datafields["S"][key] = temp
        elif key == "M":
            while temp > 9999:
                temp = int(input("INPUT CHARACTER HOST HEALTH (MAX 9999): "))
            datafields["S"][key] = temp
        elif key == "J":
            while temp > 100:
                temp = int(input("INPUT CHARACTER SHIELD RECHARGE RATE (MAX 100%): "))
            datafields["S"][key] = temp
        elif key == "O":
            while temp > 100:
                temp = int(input("INPUT CHARACTER ABILITY TO OVERTAKE HOST (MAX 100%): "))
            datafields["S"][key] = temp
        elif key == "A":
            while temp > 999:
                temp = int(input("INPUT CHARACTER BASE ATTACK (MAX 999): "))
            datafields["S"][key] = temp
        elif key == "D":
            while temp > 999:
                temp = int(input("INPUT CHARACTER BASE DEFENSE (MAX 999): "))
            datafields["S"][key] = temp
        elif key == "Q":
            while temp > 100:
                temp = int(input("INPUT CHARACTER BASE SPEED (MAX 100): "))
            datafields["S"][key] = temp
        elif key == "I":
            while temp > 100:
                temp = int(input("INPUT CHARACTER BASE INTELLIGENCE (MAX 100): "))
            datafields["S"][key] = temp
        elif key == "E":
            while temp > 100:
                temp = int(input("INPUT CHARACTER BASE ENDURANCE (MAX 100): "))
            datafields["S"][key] = temp
        elif key == "P":
            while temp > 100:
                temp = int(input("INPUT CHARACTER BASE STRENGTH (MAX 100): "))
            datafields["S"][key] = temp
        elif key == "W":
            while temp > 100:
                temp = int(input("INPUT CHARACTER BASE LUCK (MAX 100): "))
            datafields["S"][key] = temp
        elif key == "G":
            while temp > 100:
                temp = int(input("INPUT CHARACTER BASE FIREARMS SKILL (MAX 100): "))
            datafields["S"][key] = temp
        else:
            break
    write_step()


def strip_specials(user_input):
    lib = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    out_name = ''
    for char in user_input:
        if char in lib:
            out_name += char
    return out_name


def type_check(input_type):
    lib = 'CPENLV'
    if input_type not in lib:
        return 'N'
    else:
        return input_type.upper()


def write_step():
    with open("main.json", 'w+') as json_dumpfile:
        json.dump(datafields, json_dumpfile, separators=(',', ':'))
        json_dumpfile.close()

characteristics()
utilities()
weapon_main()
weapon_secondary()
character_stats()


