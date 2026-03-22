import os

if os.path.isfile("to_remove"):
    os.remove("to_remove")
else:
    os.rmdir("to_remove")
