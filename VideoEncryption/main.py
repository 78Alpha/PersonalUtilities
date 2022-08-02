import subprocess
import glob
import base64
import os
import tqdm
import argparse
import sys

VERSION: str = '0.0.2'
apm = argparse.ArgumentParser(prog='BMPMOT')
apm.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the file')
apm.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the file')
apm.add_argument('--version', '-v', action='version', version=f"%(prog)s {VERSION}")
args = vars(apm.parse_args())

_C_KEY_ = "ajdutijklomsnideowpj72980ru9ef02" # 32 character key
_C_IV_ = _C_KEY_

if not os.path.exists("./input"):
    os.mkdir("./input")
if not os.path.exists("./output"):
    os.mkdir("./output")
if not os.path.exists("./temp"):
    os.mkdir("./temp")
if not os.path.exists("./tools"):
    os.mkdir("./tools")


if not os.path.isfile("./tools/mp4encrypt.exe"):
    print("MP4DECRYPT MISSING!\n")
    sys.exit(1)

if not os.path.isfile("./tools/mp4decrypt.exe"):
    print("MP4DECRYPT MISSING!\n")
    sys.exit(1)

if not os.path.isfile("./tools/mp4fragment.exe"):
    print("MP4FRAGMENT MISSING!\n")
    sys.exit(1)


def encrypt(base64_name):
    print("Encrypting...")
    target = f"{os.getcwd()}\\temp\\{base64_name}.frag.mp4"
    output_target = f"{os.getcwd()}\\output\\{base64_name}.enc.mp4"
    td = f"1:{_C_KEY_}:{_C_IV_}"
    subprocess.call(f"powershell .\\tools\\mp4encrypt.exe --method MPEG-CENC --key {td} \"{target}\" \"{output_target}\"", shell=True)
    pass


def decrypt(file):
    print("Decrypting...")
    base_name = os.path.basename(file)
    base64_part = base_name.split(".")[0]
    base64_name = base64.b64decode(base64_part).decode()
    td = f"1:{_C_KEY_}"
    subprocess.call(f"powershell .\\tools\\mp4decrypt.exe --show-progress --key {td} \"{file}\" \"{os.getcwd()}\\output\\{base64_name}\"", shell=True)
    pass


def fragment(file):
    print("Fragmenting...")
    file_name = os.path.basename(file)
    base64_name = base64.b64encode(file_name.encode()).decode()
    subprocess.call(f"powershell .\\tools\\mp4fragment.exe \"{file}\" \"{os.getcwd()}\\temp\\{base64_name}.frag.mp4\"", shell=True)
    return base64_name


def remove_bad_characters(target):
    bad_characters = ["'", '<', '>', '"', '|', '?', '*', '[', ']', '{', '}', '`', '~', '!', '@', '#', '$', '%', '-', '^', '&', '*', '(', ')', '+', '=', ';', ',']
    output_name = target
    for bad_character in bad_characters:
        if bad_character in output_name:
            output_name = output_name.replace(bad_character, '')
    return output_name


def main():
    file_list = glob.glob(f"{os.getcwd()}\\input\\*.*")
    for filex in tqdm.tqdm(file_list):
        file = remove_bad_characters(filex).replace(" ", "_")
        print(file)
        os.rename(filex, file)
        if args['encrypt']:
            name = fragment(file)
            encrypt(name)
        elif args['decrypt']:
            decrypt(file)
        else:
            print("No action specified")


if __name__ == "__main__":
    main()
