import fnmatch
import os

for filename in os.listdir('.'):
    if fnmatch.fnmatch(filename, '*.py'):
        print(filename)
