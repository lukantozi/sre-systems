import shutil

trash_dir = 'to_remove/level1'
try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir}: {e.strerror}')
