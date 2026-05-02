import tempfile
import os

with tempfile.TemporaryDirectory() as tmpdir:
    print("Created temporary directory: ", tmpdir)
    print(os.path.exists(tmpdir))

print(os.path.exists(tmpdir))
