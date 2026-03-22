import os

for dirpath, dirnames, files in os.walk('.'):
#    print(f'In directory: {dirpath}')
    print(f'dirname: {dirnames}')
    print(f'files: {files}')
#    for file in files:
#        print(file)
