import json

datafields = {
    "C": f"{'x'*12}",  # CODENAME
    "N": f"{'x'*28}",  # NAME
    "T": f"{'x'*1}",  # TYPE
    "U": {  # UTILITIES
        "H": f"{'x'*12}",  # HEAD
        "E": f"{'x'*12}",  # EYES
        "F": f"{'x'*12}",  # FACE
        "O": f"{'x'*12}",  # OUTERWEAR
        "I": f"{'x'*12}",  # INNERWEAR
        "L": f"{'x'*12}",  # LOWERWEAR
        "G": f"{'x'*12}",  # GLOVES
        "S": f"{'x'*12}",  # SHOES
    },
    "H": {  # MAIN
        "N": f"{'x'*10}",  # NAME
        "A": 100,  # ATTACK POWER
        "T": f"{'x'*1}",  # TYPE
        "R": 100,  # RATE OF ATTACK
        "L": 100,  # RELOAD TIME
        "C": 100  # CAPACITY
    },
    "L": {  # SUB
        "N": f"{'x'*10}",  # NAME
        "A": 100,  # ATTACK POWER
        "T": f"{'x'*1}",  # TYPE
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


# with open("testfile4.json", 'w+') as json_dumpfile:
#     json.dump(datafields, json_dumpfile, separators=(',', ':'))
#     json_dumpfile.close()


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


def check_keys():
    for key, value in datafields.items():
        if type(value) == str:
            if key == "C":
                temp = f"{'x'*100}"
                while len(temp) > 12:
                    temp = input("INPUT CODENAME (MAX 12 CHARACTERS, SPECIALS WILL BE STRIPPED): ")
                    temp2 = strip_specials(temp)
                datafields[key] = temp2

            if key == "N":
                temp = f"{'x'*100}"
                while len(temp) > 28:
                    temp = input("INPUT NAME (MAX 12 CHARACTERS, SPECIALS WILL BE STRIPPED): ")
                    temp2 = strip_specials(temp)
                datafields[key] = temp2

            if key == "T":
                temp = f"{'x'*100}"
                while len(temp) > 1:
                    temp = input("INPUT TYPE (MAX 1 CHARACTERS, SPECIALS WILL BE STRIPPED, CHECK GUIDE FOR VALID TYPES): ")
                    temp2 = strip_specials(temp)
                    temp3 = type_check(temp2)
                datafields[key] = temp3
                
        if type(value) == dict:
            if key == "U":
                print("\nUTILITIES [CLOTHING]\n")
            if key == "H":
                print("\nWEAPON [MAIN]\n")
            if key == "L":
                print("\nWEAPON [SECONDARY]\n")
            if key == "S":
                print("\nCHARACTER [STATS]\n")
            for inner_key, inner_value in value.items():
                if inner_key == "N":
                    temp = f"{'x' * 100}"
                    while len(temp) > 10:
                        temp = input("INPUT NAME (MAX 10 CHARACTERS, SPECIALS WILL BE STRIPPED): ")
                        temp2 = strip_specials(temp2)
                    datafields[key][inner_key] = temp

                if inner_key == "T":
                    temp = f"{'x' * 100}"
                    while len(temp) > 1:
                        temp = input(
                            "INPUT NAME (MAX 1 CHARACTERS, SPECIALS WILL BE STRIPPED, CHECK GUIDE FOR VALID TYPES): ")
                        temp2 = strip_specials(temp)
                        temp3 = type_check(temp2)
                        datafields[key][inner_key] = temp

                if inner_key == "H" or inner_key == "S" or inner_key == "M":
                    temp = 10000
                    if inner_key == "H":
                        message = "CHARACTER BASE HP"
                    if inner_key == "S":
                        message = "CHARACTER BASE SHIELD"
                    if inner_key == "M":
                        message = "ENTER HOST HP (REQUIRED EVEN FOR HOST)"
                    while temp == 0 or temp > 9999:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 9999): "))
                    datafields[key][inner_key] = temp

                if inner_key == "A":
                    temp = 1000
                    message = "BASE ATTACK POWER"
                    while temp == 0 or temp > 999:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 999): "))
                    datafields[key][inner_key] = temp

                if inner_key == "R":
                    temp = 1000
                    message = "WEAPON RATE OF FIRE"
                    while temp == 0 or temp > 999:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 999): "))
                    datafields[key][inner_key] = temp

                if inner_key == "L":
                    temp = 1000
                    message = "RELOAD TIME (INPUT 1 for MELEE)"
                    while temp == 0 or temp > 999:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 999): "))
                    datafields[key][inner_key] = temp

                if inner_key == "C":
                    temp = 1000
                    message = "WEAPON AMMO CAPACITY (ENTER 999 for MELEE)"
                    while temp == 0 or temp > 999:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 999): "))
                    datafields[key][inner_key] = temp

                if inner_key == "J":
                    temp = 1000
                    message = "SHIELD RECHARGE RATE"
                    while temp == 0 or temp > 999:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 999): "))
                    datafields[key][inner_key] = temp

                if inner_key == "O":
                    temp = 1000
                    message = "TIME IN SECONDS FOR AGENT TO OVERTAKE HOST"
                    while temp == 0 or temp > 100:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 100): "))
                    datafields[key][inner_key] = temp

                if inner_key == "D":
                    temp = 1000
                    message = "BASE DEFENSE STAT"
                    while temp == 0 or temp > 100:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 100): "))
                    datafields[key][inner_key] = temp

                if inner_key == "Q":
                    temp = 1000
                    message = "BASE SPEED STAT"
                    while temp == 0 or temp > 100:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 100): "))
                    datafields[key][inner_key] = temp

                if inner_key == "I":
                    temp = 1000
                    message = "BASE INTELLIGENCE STAT"
                    while temp == 0 or temp > 100:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 100): "))
                    datafields[key][inner_key] = temp

                if inner_key == "E":
                    temp = 1000
                    message = "BASE ENDURANCE STAT"
                    while temp == 0 or temp > 100:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 100): "))
                    datafields[key][inner_key] = temp

                if inner_key == "P":
                    temp = 1000
                    message = "BASE STRENGTH STAT"
                    while temp == 0 or temp > 100:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 100): "))
                    datafields[key][inner_key] = temp

                if inner_key == "W":
                    temp = 1000
                    message = "BASE LUCK STAT"
                    while temp == 0 or temp > 100:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 100): "))
                    datafields[key][inner_key] = temp

                if inner_key == "G":
                    temp = 1000
                    message = "BASE GUN-HANDLING STAT"
                    while temp == 0 or temp > 100:
                        temp = int(input(f"INPUT {message} (LIMIT MAX 100): "))
                    datafields[key][inner_key] = temp

        # print(f"{key} | {value}") if type(value) == str else print("DICT")
        # print(type(value))


check_keys()
with open("main.json", 'w+') as json_dumpfile:
    json.dump(datafields, json_dumpfile, separators=(',', ':'))
    json_dumpfile.close()
