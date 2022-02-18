import os
from pathlib import Path

current_path = Path.cwd() / "images"


def main():
    i = 0
    for filename in os.listdir(current_path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = current_path / filename
        my_dest = current_path / my_dest
        os.rename(my_source, my_dest)
        i += 1


if __name__ == '__main__':
    main()