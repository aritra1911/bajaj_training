import os
from typing import Dict

def main() -> None:
    dir = 'bajaj_training/python'
    files = [
        os.path.join(dir, f)
        for f in os.listdir(dir)
        if os.path.isfile(os.path.join(dir, f))
    ]
    files.sort(key=lambda file: os.path.getsize(file))
    print(files)

if __name__ == '__main__':
    main()