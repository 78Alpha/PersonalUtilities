import base64
import glob
import os
import tqdm


def main():
    webp_files = glob.glob('./**/*.webp', recursive=True)
    for file in tqdm.tqdm(webp_files):
        base_name = os.path.basename(file)
        name_part = base_name.split('.webp')[0]
        base64_name = base64.b64encode(name_part.encode('utf-8')).decode('utf-8')
        new_name = base64_name + '.webp'
        os.rename(file, new_name)


if __name__ == '__main__':
    main()
