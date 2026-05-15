import unittest
from file_storage_impl import FileStorageImpl

class Level1Tests(unittest.TestCase):
    def setUp(self):
        self.fs = FileStorageImpl()

    def test_upload_and_get(self):
        self.fs.file_upload("Cars.txt", 200_000)
        self.assertEqual(self.fs.file_get("Cars.txt"), 200_000)

    def test_get_missing(self):
        self.assertIsNone(self.fs.file_get("missing.txt"))

    def test_upload_duplicate_raises(self):
        self.fs.file_upload("a.bin", 10)
        with self.assertRaises(RuntimeError):
            self.fs.file_upload("a.bin", 11)

    def test_copy_missing_source_raises(self):
        with self.assertRaises(RuntimeError):
            self.fs.file_copy("missing.txt", "dest.txt")

    def test_copy_creates_dest(self):
        self.fs.file_upload("a.txt", 123)
        self.fs.file_copy("a.txt", "b.txt")
        self.assertEqual(self.fs.file_get("b.txt"), 123)

    def test_copy_overwrites_dest(self):
        self.fs.file_upload("a.txt", 123)
        self.fs.file_upload("b.txt", 999)
        self.fs.file_copy("a.txt", "b.txt")
        self.assertEqual(self.fs.file_get("b.txt"), 123)
