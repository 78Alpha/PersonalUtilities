import os
import glob

dir = glob.glob(f"{os.getcwd()}/*/")

for folder in dir:
    print(folder)
    folder = folder[:-1]
    os.system(f"tar.exe -cf \"{folder}.cbz\"  -C \"{folder}\" \"*\"")