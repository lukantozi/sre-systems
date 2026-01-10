import unittest
from file_storage_impl import FileStorageImpl

class Level2Tests(unittest.TestCase):
    def setUp(self):
        self.fs = FileStorageImpl()

    def test_search_empty(self):
        self.assertEqual(self.fs.file_search("a"), [])

    def test_search_prefix_sorted(self):
        self.fs.file_upload("app.log", 100)
        self.fs.file_upload("apple.txt", 100)
        self.fs.file_upload("api.txt", 250)
        self.fs.file_upload("banana.txt", 999)

        # Matches: api.txt(250), app.log(100), apple.txt(100)
        # Tie on 100 -> name asc: app.log before apple.txt
        self.assertEqual(
            self.fs.file_search("ap"),
            ["api.txt(250)", "app.log(100)", "apple.txt(100)"]
        )

    def test_search_updates_after_copy(self):
        self.fs.file_upload("a.txt", 10)
        self.fs.file_copy("a.txt", "ab.txt")
        self.assertEqual(self.fs.file_search("a"), ["a.txt(10)", "ab.txt(10)"])

    def test_search_top_10_limit(self):
        for i in range(20):
            self.fs.file_upload(f"a{i}", i)  # sizes 0..19

        res = self.fs.file_search("a")
        self.assertEqual(len(res), 10)
        self.assertEqual(res[0], "a19(19)")
        self.assertEqual(res[-1], "a10(10)")
