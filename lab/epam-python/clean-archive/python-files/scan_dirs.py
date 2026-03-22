import os

with os.scandir('../../') as entries:
    for entry in entries:
        if entry.is_dir():
            print(entry.name)
