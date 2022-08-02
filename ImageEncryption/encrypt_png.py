import os
import glob

file_list = glob.glob("./*.png")

for file in file_list:
    out_name = file.replace(".png", ".enc")
    os.system(f"magick \"{file}\" -encipher passphrase.txt \"{out_name}.png\"")