import PySimpleGUI as gui
import tarfile
import os
import base64
import json
from PIL import Image
import io

_VERSION_ = '0.1.1'

_TYPE_SCHEMA_ = ["NORMAL", "CHAOS", "PSYONICS", "KINETICS", "ENERGY", "ARCANIC"]

_CHARACTER_ = {
    "codename": "",  # CODENAME
    "name": "",  # NAME
    "level": 0,  # LEVEL
    "class": "NORMAL",  # TYPE
    "description": "",  # DESCRIPTION
    "images": {
        "headshot": "",  # HEADSHOT Size : (4096, 4096)
        "background": "",  # BACKGROUND Size : (4096, 4096)
        "portrait": "",  # PORTRAIT Size : (1024, 4096)
        "icon": "",  # ICON Size : (512, 512)
        "animation_archive": "",  # ANIMATION_ARCHIVE Compress as XZ file or LZMA data
    },
    "clothing": {  # UTILITIES
        "head": "",  # HEAD
        "eyes": "",  # EYES
        "face": "",  # FACE
        "outerwear": "",  # OUTERWEAR
        "innerwear": "",  # INNERWEAR
        "lowerwear": "",  # LOWERWEAR
        "gloves": "",  # GLOVES
        "shoes": "",  # SHOES
    },
    "mainweapon": {  # MAIN
        "name": "",  # NAME
        "level": 0,
        "attack": 0,  # ATTACK POWER
        "class": "NORMAL",  # TYPE
        "rateoffire": 0,  # RATE OF ATTACK
        "reloadspeed": 0,  # RELOAD TIME
        "ammo": 0,  # CAPACITY
        "value": 0,  # VALUE
        "description": "",  # DESCRIPTION
    },
    "subweapon": {  # SUB
        "name":"",  # NAME
        "level": 0,
        "attack": 0,  # ATTACK POWER
        "class": "NORMAL",  # TYPE
        "rateoffire": 0,  # RATE OF ATTACK
        "reloadspeed": 0,  # RELOAD TIME
        "ammo": 0,  # CAPACITY
        "value": 0,  # VALUE
        "description": "",  # DESCRIPTION
    },
    "characterstats": {  # BASE STATS
        "health": 0,  # MAIN HEALTH
        "shield": 0,  # REGENERATING SHIELD
        "hosthealth": 0,  # HOST HP AFTER DETACH
        "shieldrecharge": 0,  # SHIELD RECHARGE RATE
        "overtake": 0,  # ABILITY TO OVERTAKE HOST AFTER DETACH
        "attack": 0,  # BASE ATTACK
        "defense": 0,  # BASE DEFENSE
        "speed": 0,  # BASE SPEED
        "intelligence": 0,  # BASE INTELLIGENCE
        "endurance": 0,  # BASE ENDURANCE
        "strength": 0,  # BASE STRENGTH
        "luck": 0,  # BASE LUCK
        "gunhandling": 0,  # BASE FIREARMS HANDLING
        "stagger": 0,  # BASE STAGGER
    }
}

_C_BLANK_ = _CHARACTER_

_WEAPON_ = {
    "name": "",  # NAME
    "level": 0,
    "images": {
        "background": "",  # BACKGROUND Size : (4096, 4096)
        "portrait": "",  # PORTRAIT Size : (1024, 4096)
        "icon": "",  # ICON Size : (512, 512)
        "animation_archive": "",  # ANIMATION_ARCHIVE Compress as XZ file or LZMA data
    },
    "attack": 0,  # ATTACK POWER
    "class": "NORMAL",  # TYPE
    "rateoffire": 0,  # RATE OF ATTACK
    "reloadspeed": 0,  # RELOAD TIME
    "ammo": 0,  # CAPACITY
    "description": "",  # DESCRIPTION
    "value": 0  # VALUE
}


_W_BLANK_ = _WEAPON_


_CLOTHING_ = {
    "name": "",  # NAME
    "class": "",  # TYPE
    "images": {
        "background": "",  # BACKGROUND Size : (4096, 4096)
        "portrait": "",  # PORTRAIT Size : (1024, 4096)
        "icon": "",  # ICON Size : (512, 512)
        "animation_archive": "",  # ANIMATION_ARCHIVE Compress as XZ file or LZMA data
    },
    "description": "",  # DESCRIPTION
    "resistance": "",  # class of resistance
    "resist": 0,  # resistance percentage
    "value": 0,  # VALUE
    "statadditions": {  # ADDITIONS
        "health": 0,  # HEALTH
        "hosthealth": 0,  # HOST HP AFTER DETACH
        "shield": 0,  # SHIELD
        "attack": 0,  # ATTACK
        "defense": 0,  # DEFENSE
        "speed": 0,  # SPEED
        "intelligence": 0,  # INTELLIGENCE
        "endurance": 0,  # ENDURANCE
        "strength": 0,  # STRENGTH
        "luck": 0,  # LUCK
        "gunhandling": 0,  # FIREARMS HANDLING
        "stagger": 0,  # STAGGER
    }
}

_ITEM_ = {
    "name": "",  # NAME
    "value": 0,  # VALUE
    "images": {
        "background": "",  # BACKGROUND Size : (4096, 4096)
        "portrait": "",  # PORTRAIT Size : (1024, 4096)
        "icon": "",  # ICON Size : (512, 512)
        "animation_archive": "",  # ANIMATION_ARCHIVE Compress as XZ file or LZMA data
    },
    "description": "",  # DESCRIPTION
    "duration": 0,  # DURATION
    "uses": 0,  # USES
    "statadditions": {  # ADDITIONS
        "health": 0,  # HEALTH
        "hosthealth": 0,  # HOST HP AFTER DETACH
        "shield": 0,  # SHIELD
        "attack": 0,  # ATTACK
        "defense": 0,  # DEFENSE
        "speed": 0,  # SPEED
        "intelligence": 0,  # INTELLIGENCE
        "endurance": 0,  # ENDURANCE
        "strength": 0,  # STRENGTH
        "luck": 0,  # LUCK
        "gunhandling": 0,  # FIREARMS HANDLING
        "stagger": 0,  # STAGGER
    }
}


def scale_base64_image(base64_image, width, height):
    # Decode base64 image
    image_data = base64.b64decode(base64_image)
    # scale image to width and height
    image = Image.open(io.BytesIO(image_data))
    image = image.convert("RGBA")
    image = image.resize((width, height), Image.ANTIALIAS)
    # convert image to base64
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def compress_animation(character_name, input_directory):
    # compress the directory input_directory into a tar.xz file
    # file should be named character_name_animation.tar.xz
    with tarfile.open(character_name + "_animation.tar.xz", "w:xz") as tar:
        tar.add(input_directory, arcname=os.path.basename(input_directory))
    # open the tar.xz file and read the data into memory
    # convert data into base64 and return it
    with open(character_name + "_animation.tar.xz", "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")


def convert_image(image_path):
    # convert the image into a base64 string
    # return the base64 string
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")
    pass


def save_data(dict_data, file_name):
    # save the data of dict_data into json file
    # file should be named file_name.json
    with open(file_name + ".json", "w") as f:
        json.dump(dict_data, f)


def weapon_window():
    global _WEAPON_
    # create window for weapon using PySimpleGUI
    # window should contain elements for key in _WEAPON_
    # window should contain a button to save the data
    # window should contain a button to clear the data
    # window should contain a button to close the window
    weapon_layout = [
        [gui.Text("Weapon")],
        [gui.Text("Name"), gui.InputText(key="name")],
        [gui.Text("Level"), gui.Spin([i for i in range(100)], size=(5, 1), key="level")],
        [gui.Text("Images")],
        [gui.Text("Background"), gui.InputText(key="background"), gui.FileBrowse(file_types=(("PNG", "*.png"),), enable_events=True)],
        [gui.Text("Portrait"), gui.InputText(key="portrait"), gui.FileBrowse(file_types=(("PNG", "*.png"),), enable_events=True)],
        [gui.Text("Icon"), gui.InputText(key="icon"), gui.FileBrowse(file_types=(("PNG", "*.png"),), enable_events=True)],
        [gui.Frame(title='', key="frame", size=(420, 140), layout=[[gui.Image(data=scale_base64_image(convert_image("./caution.jpg"), 128, 128), size=(128, 128), key="background_image"), gui.Image(data=scale_base64_image(convert_image("./caution.jpg"), 128, 128), size=(128, 128), key="portrait_image"), gui.Image(data=scale_base64_image(convert_image("./caution.jpg"), 128, 128), size=(128, 128), key="icon_image")]])],
        [gui.Text("Animation Archive"), gui.InputText(key="animation_archive"), gui.FolderBrowse(enable_events=True)],
        [gui.Text("Attack"), gui.Spin([i for i in range(100)], size=(5, 1), key="attack")],
        [gui.Text("Class"), gui.DropDown(_TYPE_SCHEMA_, default_value=_TYPE_SCHEMA_[0], size=(20, 1), key="class")],
        [gui.Text("Rate of Fire"), gui.Spin([i for i in range(100)], size=(5, 1), key="rate_of_fire")],
        [gui.Text("Reload Speed"), gui.Spin([i for i in range(100)], size=(5, 1), key="reload_speed")],
        [gui.Text("Ammo"), gui.Spin([i for i in range(1000)], size=(5, 1), key="ammo")],
        [gui.Text("Value"), gui.Spin([i for i in range(1000)], size=(5, 1), key="value")],
        [gui.Text("Description"), gui.Multiline(size=(20, 3), key="description")],
        # [gui.Button("Refresh", enable_events=True), gui.Button("Save", enable_events=True), gui.Button("Clear", enable_events=True), gui.Button("Close", enable_events=True)],
        [gui.Button("Refresh", enable_events=True),
         gui.InputText('', visible=False, key="target", enable_events=True),
         gui.SaveAs('Save', target='target', default_extension=".json", file_types=(("JSON", "*.json"),),
                    enable_events=True, key='Save'),
         gui.FileBrowse("Load", target='target', enable_events=True, file_types=(("JSON", ".json"),), key='Load'),
         gui.Button("Clear", enable_events=True), gui.Button('Close', enable_events=True)]

    ]

    window = gui.Window("Weapon", layout=weapon_layout)
    while True:
        event, values = window.read()
        if event in (None, "Close"):
            window.Close()
            break
        elif event == "Save":
            print("Saving Weapon")
            _WEAPON_["name"] = values["name"]
            _WEAPON_["level"] = values["level"]
            _WEAPON_["images"]["background"] = convert_image(values["background"])
            _WEAPON_["images"]["portrait"] = convert_image(values["portrait"])
            _WEAPON_["images"]["icon"] = convert_image(values["icon"])
            _WEAPON_["images"]["animation_archive"] = compress_animation(values["name"], values["animation_archive"])
            _WEAPON_["attack"] = values["attack"]
            _WEAPON_["class"] = values["class"]
            _WEAPON_["rate_of_fire"] = values["rate_of_fire"]
            _WEAPON_["reload_speed"] = values["reload_speed"]
            _WEAPON_["ammo"] = values["ammo"]
            _WEAPON_["value"] = values["value"]
            _WEAPON_["description"] = values["description"]
            # save_data(_WEAPON_, "weapon")
            with open(values["target"], 'w+') as f:
                json.dump(_CHARACTER_, f, indent=3)
                f.close()
        elif event == "Load":
            with open(values['target'], 'r') as f:
                _WEAPON_ = json.load(f)
            values['load'] = ''
            window.Refresh()
        elif event == "Clear":
            print("Clear")
            _WEAPON_ = _W_BLANK_
            window.close()
            weapon_window()
        elif event == "Refresh":
            print("Refresh")
            # window.find_element("column").update(visible=True)
            window.find_element("background_image").update(data=scale_base64_image(convert_image(values["background"]), 128, 128), visible=True) if values["background"] else window.find_element("background_image").update(visible=False)
            window.find_element("portrait_image").update(data=scale_base64_image(convert_image(values["portrait"]), 128, 128), visible=True) if values["portrait"] else window.find_element("portrait_image").update(visible=False)
            window.find_element("icon_image").update(data=scale_base64_image(convert_image(values["icon"]), 128, 128), visible=True) if values["icon"] else window.find_element("icon_image").update(visible=False)
            if values["Save"] != '':
                print("Saving Weapon")
                _WEAPON_["name"] = values["name"]
                _WEAPON_["images"]["background"] = convert_image(values["background"])
                _WEAPON_["images"]["portrait"] = convert_image(values["portrait"])
                _WEAPON_["images"]["icon"] = convert_image(values["icon"])
                _WEAPON_["images"]["animation_archive"] = compress_animation(values["name"],
                                                                             values["animation_archive"])
                _WEAPON_["attack"] = values["attack"]
                _WEAPON_["class"] = values["class"] if values["class"] in _TYPE_SCHEMA_ else _TYPE_SCHEMA_[0]
                _WEAPON_["rate_of_fire"] = values["rate_of_fire"]
                _WEAPON_["reload_speed"] = values["reload_speed"]
                _WEAPON_["ammo"] = values["ammo"]
                _WEAPON_["value"] = values["value"]
                _WEAPON_["description"] = values["description"]
                # save_data(_WEAPON_, "weapon")
                with open(values["target"], 'w+') as f:
                    json.dump(_CHARACTER_, f, indent=3)
                    f.close()
                window.find_element("target").Update('')
            if values["Load"] != '':
                with open(values['target'], 'r') as f:
                    _WEAPON_ = json.load(f)
                window.find_element("target").Update('')
            window.Refresh()
        elif event == "Close":
            print("Close")
            window.close()
            break
    pass


def character_window():
    global _CHARACTER_
    character_tab = [
        [gui.Text("Name"), gui.InputText(size=(20, 1), key='name', default_text=_CHARACTER_["name"]), gui.Text("Codename"),
         gui.InputText(size=(20, 1), key='codename', default_text=_CHARACTER_["codename"])],
        [gui.Text("Level"), gui.Spin([i for i in range(100)], size=(5, 1), key='level', initial_value=_CHARACTER_["level"])],
        [gui.Text("Class"), gui.DropDown(_TYPE_SCHEMA_, default_value=_CHARACTER_["class"], size=(20, 1), key='class')],
        [gui.Text("Stats")],
        [gui.Text("Health"), gui.Spin([i for i in range(9999)], size=(5, 1), key='stats.health', initial_value=_CHARACTER_["characterstats"]["health"])],
        [gui.Text("Host Health"), gui.Spin([i for i in range(9999)], size=(5, 1), key='stats.hosthealth', initial_value=_CHARACTER_["characterstats"]["hosthealth"])],
        [gui.Text("Shield"), gui.Spin([i for i in range(9999)], size=(5, 1), key='stats.shield', initial_value=_CHARACTER_["characterstats"]["shield"])],
        [gui.Text("Recharge"), gui.Spin([i for i in range(100)], size=(5, 1), key='stats.recharge', initial_value=_CHARACTER_["characterstats"]["shieldrecharge"])],
        [gui.Text("overtake"), gui.Spin([i for i in range(9999)], size=(5, 1), key='stats.overtake', initial_value=_CHARACTER_["characterstats"]["overtake"])],
        [gui.Text("Attack"), gui.Spin([i for i in range(1000)], size=(5, 1), key='stats.attack', initial_value=_CHARACTER_["characterstats"]["attack"])],
        [gui.Text("Defense"), gui.Spin([i for i in range(1000)], size=(5, 1), key='stats.defense', initial_value=_CHARACTER_["characterstats"]["defense"])],
        [gui.Text("Speed"), gui.Spin([i for i in range(100)], size=(5, 1), key='stats.speed', initial_value=_CHARACTER_["characterstats"]["speed"])],
        [gui.Text("Intelligence"), gui.Spin([i for i in range(100)], size=(5, 1), key='stats.intelligence', initial_value=_CHARACTER_["characterstats"]["intelligence"])],
        [gui.Text("Endurance"), gui.Spin([i for i in range(100)], size=(5, 1), key='stats.endurance', initial_value=_CHARACTER_["characterstats"]["endurance"])],
        [gui.Text("Strength"), gui.Spin([i for i in range(100)], size=(5, 1), key='stats.strength', initial_value=_CHARACTER_["characterstats"]["strength"])],
        [gui.Text("Luck"), gui.Spin([i for i in range(100)], size=(5, 1), key='stats.luck', initial_value=_CHARACTER_["characterstats"]["luck"])],
        [gui.Text("Description"), gui.Multiline(size=(20, 3), key='description', default_text=_CHARACTER_["description"])],
        ]

    weapons_tab = [
        [gui.Text("Main Weapon")],
        [gui.Text("Name"), gui.InputText(size=(20, 1), key='mainweapon.name', default_text=_CHARACTER_["mainweapon"]["name"])],
        [gui.Text("Level"), gui.Spin([i for i in range(100)], size=(5, 1), key='mainweapon.level', initial_value=_CHARACTER_["mainweapon"]["level"])],
        [gui.Text("Attack"), gui.Spin([i for i in range(1000)], size=(20, 1), key='mainweapon.attack', initial_value=_CHARACTER_["mainweapon"]["attack"])],
        [gui.Text("Class"), gui.DropDown(_TYPE_SCHEMA_, default_value=_CHARACTER_["mainweapon"]["class"], size=(20, 1), key='mainweapon.class')],
        [gui.Text("Rate of Fire"), gui.Spin([i for i in range(1000)], size=(20, 1), key='mainweapon.rateoffire', initial_value=_CHARACTER_["mainweapon"]["rateoffire"])],
        [gui.Text("Reload Speed"), gui.Spin([i for i in range(100)], size=(5, 1), key='mainweapon.reloadspeed', initial_value=_CHARACTER_["mainweapon"]["reloadspeed"])],
        [gui.Text("Ammo"), gui.Spin([i for i in range(1000)], size=(5, 1), key='mainweapon.ammo', initial_value=_CHARACTER_["mainweapon"]["ammo"])],
        [gui.Text("Value"), gui.Spin([i for i in range(1000)], size=(5, 1), key='mainweapon.value', initial_value=_CHARACTER_["mainweapon"]["value"])],
        [gui.Text("Description"), gui.Multiline(size=(20, 3), key='mainweapon.description', default_text=_CHARACTER_["mainweapon"]["description"])],
        [gui.Text("Secondary Weapon")],
        [gui.Text("Name"), gui.InputText(size=(20, 1), key='secondaryweapon.name', default_text=_CHARACTER_["subweapon"]["name"])],
        [gui.Text("Level"), gui.Spin([i for i in range(100)], size=(5, 1), key='secondaryweapon.level', initial_value=_CHARACTER_["subweapon"]["level"])],
        [gui.Text("Attack"), gui.Spin([i for i in range(1000)], size=(20, 1), key='secondaryweapon.attack', initial_value=_CHARACTER_["subweapon"]["attack"])],
        [gui.Text("Class"), gui.DropDown(_TYPE_SCHEMA_, default_value=_CHARACTER_["subweapon"]["class"], size=(20, 1), key='secondaryweapon.class')],
        [gui.Text("Rate of Fire"), gui.Spin([i for i in range(1000)], size=(20, 1), key='secondaryweapon.rateoffire', initial_value=_CHARACTER_["subweapon"]["rateoffire"])],
        [gui.Text("Reload Speed"), gui.Spin([i for i in range(100)], size=(5, 1), key='secondaryweapon.reloadspeed', initial_value=_CHARACTER_["subweapon"]["reloadspeed"])],
        [gui.Text("Ammo"), gui.Spin([i for i in range(1000)], size=(5, 1), key='secondaryweapon.ammo', initial_value=_CHARACTER_["subweapon"]["ammo"])],
        [gui.Text("Value"), gui.Spin([i for i in range(1000)], size=(5, 1), key='secondaryweapon.value', initial_value=_CHARACTER_["subweapon"]["value"])],
        [gui.Text("Description"), gui.Multiline(size=(20, 3), key='secondaryweapon.description', default_text=_CHARACTER_["subweapon"]["description"])],
    ]

    clothing_tab = [
        [gui.Text("Clothing")],
        [gui.Text("Head"), gui.InputText(size=(20, 1), key='clothing.head', default_text=_CHARACTER_["clothing"]["head"])],
        [gui.Text("Eyes"), gui.InputText(size=(20, 1), key='clothing.eyes', default_text=_CHARACTER_["clothing"]["eyes"])],
        [gui.Text("Face"), gui.InputText(size=(20, 1), key='clothing.face', default_text=_CHARACTER_["clothing"]["face"])],
        [gui.Text("Outerwear"), gui.InputText(size=(20, 1), key='clothing.outerwear', default_text=_CHARACTER_["clothing"]["outerwear"])],
        [gui.Text("Innerwear"), gui.InputText(size=(20, 1), key='clothing.innerwear', default_text=_CHARACTER_["clothing"]["innerwear"])],
        [gui.Text("Lowerwear"), gui.InputText(size=(20, 1), key='clothing.lowerwear', default_text=_CHARACTER_["clothing"]["lowerwear"])],
        [gui.Text("Gloves"), gui.InputText(size=(20, 1), key='clothing.gloves', default_text=_CHARACTER_["clothing"]["gloves"])],
        [gui.Text("Shoes"), gui.InputText(size=(20, 1), key='clothing.shoes', default_text=_CHARACTER_["clothing"]["shoes"])],
        ]

    tabgroup = [[gui.Tab('Character', character_tab), gui.Tab('Weapons', weapons_tab), gui.Tab('Clothing', clothing_tab)]]

    character_layout = [
        [gui.Text('Character Maker', size=(20, 1), font=('Helvetica', 20), justification='center')],
        [gui.TabGroup(tabgroup)],
        [gui.Button("Refresh", enable_events=True, visible=False), gui.InputText('', visible=False, key="target", enable_events=True), gui.SaveAs('Save', target='target', default_extension=".json", file_types=(("JSON", "*.json"),), enable_events=True, key='Save'), gui.FileBrowse("Load", target='target', enable_events=True, file_types=(("JSON", ".json"),), key='Load'), gui.Button("Clear", enable_events=True), gui.Button('Close', enable_events=True)]
    ]
    char_window = gui.Window('Character', character_layout, modal=True, finalize=True)
    while True:
        event, values = char_window.Read()
        print(event, values)
        if event == 'Save':
            print('Saving Character')
            _CHARACTER_['name'] = values['name']
            _CHARACTER_['codename'] = values['codename']
            _CHARACTER_["level"] = values['level']
            _CHARACTER_['class'] = values['class'] if values["class"] in _TYPE_SCHEMA_ else _TYPE_SCHEMA_[0]
            _CHARACTER_['clothing']['head'] = values['clothing.head']
            _CHARACTER_['clothing']['eyes'] = values['clothing.eyes']
            _CHARACTER_['clothing']['face'] = values['clothing.eyes']
            _CHARACTER_['clothing']['outerwear'] = values['clothing.outerwear']
            _CHARACTER_['clothing']['innerwear'] = values['clothing.innerwear']
            _CHARACTER_['clothing']['lowerwear'] = values['clothing.lowerwear']
            _CHARACTER_['clothing']['gloves'] = values['clothing.gloves']
            _CHARACTER_['clothing']['shoes'] = values['clothing.shoes']
            _CHARACTER_['mainweapon']['name'] = values['mainweapon.name']
            _CHARACTER_['mainweapon']['level'] = values['mainweapon.level']
            _CHARACTER_['mainweapon']['attack'] = values['mainweapon.attack']
            _CHARACTER_['mainweapon']['class'] = values['mainweapon.class'] if values['mainweapon.class'] in _TYPE_SCHEMA_ else _TYPE_SCHEMA_[0]
            _CHARACTER_['mainweapon']['rateoffire'] = values['mainweapon.rateoffire']
            _CHARACTER_['mainweapon']['reloadspeed'] = values['mainweapon.reloadspeed']
            _CHARACTER_['mainweapon']['ammo'] = values['mainweapon.ammo']
            _CHARACTER_['mainweapon']['value'] = values['mainweapon.value']
            _CHARACTER_['mainweapon']['description'] = values['mainweapon.description']
            _CHARACTER_['subweapon']['name'] = values['secondaryweapon.name']
            _CHARACTER_['subweapon']['level'] = values['secondaryweapon.level']
            _CHARACTER_['subweapon']['attack'] = values['secondaryweapon.attack']
            _CHARACTER_['subweapon']['class'] = values['secondaryweapon.class'] if values['secondaryweapon.class'] in _TYPE_SCHEMA_ else _TYPE_SCHEMA_[0]
            _CHARACTER_['subweapon']['rateoffire'] = values['secondaryweapon.rateoffire']
            _CHARACTER_['subweapon']['reloadspeed'] = values['secondaryweapon.reloadspeed']
            _CHARACTER_['subweapon']['ammo'] = values['secondaryweapon.ammo']
            _CHARACTER_['subweapon']['value'] = values['secondaryweapon.value']
            _CHARACTER_['subweapon']['description'] = values['secondaryweapon.description']
            _CHARACTER_['characterstats']['health'] = values['stats.health']
            _CHARACTER_['characterstats']['hosthealth'] = values['stats.hosthealth']
            _CHARACTER_['characterstats']['shield'] = values['stats.shield']
            _CHARACTER_['characterstats']['recharge'] = values['stats.recharge']
            _CHARACTER_['characterstats']['overtake'] = values['stats.overtake']
            _CHARACTER_['characterstats']['attack'] = values['stats.attack']
            _CHARACTER_['characterstats']['defense'] = values['stats.defense']
            _CHARACTER_['characterstats']['speed'] = values['stats.speed']
            _CHARACTER_['characterstats']['intelligence'] = values['stats.intelligence']
            _CHARACTER_['characterstats']['endurance'] = values['stats.endurance']
            _CHARACTER_['characterstats']['strength'] = values['stats.strength']
            _CHARACTER_['characterstats']['luck'] = values['stats.luck']
            _CHARACTER_['description'] = values['description']
            with open(values["target"], 'w+') as f:
                json.dump(_CHARACTER_, f, indent=3)
                f.close()
        elif event == 'Load':
            print('Loading Character')
            with open(values['target'], 'r') as f:
                _CHARACTER_ = json.load(f)
            values['load'] = ''
            char_window.Refresh()
        elif event == 'Close':
            print('Closing Character')
            char_window.close()
            break
        elif event == 'Clear':
            print('Clearing Character')
            char_window.find_element('target').Update('')
            char_window.close()
            _CHARACTER_ = _C_BLANK_

            character_window()
        elif event == 'target':
            if values['Save'] != '':
                print('Saving Character')
                _CHARACTER_['name'] = values['name']
                _CHARACTER_['codename'] = values['codename']
                _CHARACTER_['class'] = values['class'] if values['class'] in _TYPE_SCHEMA_ else _TYPE_SCHEMA_[0]
                _CHARACTER_['clothing']['head'] = values['clothing.head']
                _CHARACTER_['clothing']['eyes'] = values['clothing.eyes']
                _CHARACTER_['clothing']['face'] = values['clothing.eyes']
                _CHARACTER_['clothing']['outerwear'] = values['clothing.outerwear']
                _CHARACTER_['clothing']['innerwear'] = values['clothing.innerwear']
                _CHARACTER_['clothing']['lowerwear'] = values['clothing.lowerwear']
                _CHARACTER_['clothing']['gloves'] = values['clothing.gloves']
                _CHARACTER_['clothing']['shoes'] = values['clothing.shoes']
                _CHARACTER_['mainweapon']['name'] = values['mainweapon.name']
                _CHARACTER_['mainweapon']['attack'] = values['mainweapon.attack']
                _CHARACTER_['mainweapon']['class'] = values['mainweapon.class'] if values['mainweapon.class'] in _TYPE_SCHEMA_ else _TYPE_SCHEMA_[0]
                _CHARACTER_['mainweapon']['rateoffire'] = values['mainweapon.rateoffire']
                _CHARACTER_['mainweapon']['reloadspeed'] = values['mainweapon.reloadspeed']
                _CHARACTER_['mainweapon']['ammo'] = values['mainweapon.ammo']
                _CHARACTER_['mainweapon']['value'] = values['mainweapon.value']
                _CHARACTER_['mainweapon']['description'] = values['mainweapon.description']
                _CHARACTER_['subweapon']['name'] = values['secondaryweapon.name']
                _CHARACTER_['subweapon']['attack'] = values['secondaryweapon.attack']
                _CHARACTER_['subweapon']['class'] = values['secondaryweapon.class'] if values['secondaryweapon.class'] in _TYPE_SCHEMA_ else _TYPE_SCHEMA_[0]
                _CHARACTER_['subweapon']['rateoffire'] = values['secondaryweapon.rateoffire']
                _CHARACTER_['subweapon']['reloadspeed'] = values['secondaryweapon.reloadspeed']
                _CHARACTER_['subweapon']['ammo'] = values['secondaryweapon.ammo']
                _CHARACTER_['subweapon']['value'] = values['secondaryweapon.value']
                _CHARACTER_['subweapon']['description'] = values['secondaryweapon.description']
                _CHARACTER_['characterstats']['health'] = values['stats.health']
                _CHARACTER_['characterstats']['hosthealth'] = values['stats.hosthealth']
                _CHARACTER_['characterstats']['shield'] = values['stats.shield']
                _CHARACTER_['characterstats']['recharge'] = values['stats.recharge']
                _CHARACTER_['characterstats']['overtake'] = values['stats.overtake']
                _CHARACTER_['characterstats']['attack'] = values['stats.attack']
                _CHARACTER_['characterstats']['defense'] = values['stats.defense']
                _CHARACTER_['characterstats']['speed'] = values['stats.speed']
                _CHARACTER_['characterstats']['intelligence'] = values['stats.intelligence']
                _CHARACTER_['characterstats']['endurance'] = values['stats.endurance']
                _CHARACTER_['characterstats']['strength'] = values['stats.strength']
                _CHARACTER_['characterstats']['luck'] = values['stats.luck']
                _CHARACTER_['description'] = values['description']
                with open(values["target"], 'w+') as f:
                    json.dump(_CHARACTER_, f, indent=3)
                    f.close()
                char_window.find_element('target').Update('')
                char_window.close()
                character_window()
            if values['Load'] != '':
                print('Loading Character')
                with open(values['target'], 'r') as f:
                    _CHARACTER_ = json.load(f)
                char_window.find_element('target').Update('')
                char_window.close()
                character_window()
        else:
            # global _CHARACTER_
            _CHARACTER_ = _C_BLANK_
            char_window.close()
            break


def main():
    creator_layout = [
        [gui.Text(f"Character Creator V.{_VERSION_}")],
        [gui.Button("Character", enable_events=True), gui.Button("Weapon", enable_events=True), gui.Button("Clothing", enable_events=True), gui.Button("Item", enable_events=True)],
        ]
    creator_window = gui.Window("Character Creator", creator_layout)
    while True:
        event, values = creator_window.Read()
        if event == "Character":
            print("Character")
            character_window()
        elif event == "Weapon":
            print("Weapon")
            weapon_window()
        elif event == "Clothing":
            print("Clothing")
        elif event == "Item":
            print("Item")
        elif event is None:
            break


if __name__ == "__main__":
    main()