import os
import os.path
from PIL import Image


def convertImage(path, newType):
    im = Image.open(path).convert('RGB')
    im.save(path, 'jpeg')
    print(f'converted {path} to {newType}')

def getWallpapersPath(configFile):
    with open(configFile) as f:
        lines = f.readline()
        return lines.split('=')[1].rstrip()


def main():
    path = getWallpapersPath('config.txt')

    directory = os.fsencode(path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".webp"):
            convertImage(os.path.join(directory.decode(), filename), 'jpeg')
            filename_without_type = filename.split('.')[0]
            file_path = os.path.join(directory.decode(), filename)
            new_file_path = os.path.join(directory.decode(), filename_without_type + '.jpeg')
            os.rename(file_path, new_file_path)

if __name__ == '__main__':
    main()
