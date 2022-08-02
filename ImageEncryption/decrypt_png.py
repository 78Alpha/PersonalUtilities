import os
import glob

file_list = glob.glob("./*.enc.png")

for file in file_list:
    out_name = file.replace(".enc.png", ".dec")
    os.system(f"magick \"{file}\" -decipher passphrase.txt \"{out_name}.png\"")