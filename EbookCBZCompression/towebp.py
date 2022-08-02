import glob
import os
import tqdm
import sys

while True:
    files = glob.glob("./**/*.*", recursive=True)
    #files += glob.glob("./**/*.jpg", recursive=True)
    #files += glob.glob("./**/*.jpeg", recursive=True)
    ext = ['.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff', '.gif']

    for file in tqdm.tqdm(files):
        # print(file)
        if file.endswith(tuple(ext)):
            os.system(f"cwebp -quiet -mt -z 9 -m 6 \"{file}\" -o \"{file[:-4]}.webp\"")
            os.remove(file)
        if len(files) == 0:
            sys.exit()
    sys.exit()