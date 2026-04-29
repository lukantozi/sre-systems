import unittest
from file_storage_impl import FileStorageImpl

class Level3Tests(unittest.TestCase):
    def setUp(self):
        self.fs = FileStorageImpl()

    def test_add_user(self):
        self.assertTrue(self.fs.add_user("u1", 100))
        self.assertFalse(self.fs.add_user("u1", 999))

    def test_upload_by_user_capacity(self):
        self.fs.add_user("u1", 10)
        self.assertEqual(self.fs.file_upload_by("u1", "a", 6), 4)
        self.assertIsNone(self.fs.file_upload_by("u1", "b", 5))  # would exceed
        self.assertEqual(self.fs.file_get("a"), 6)

    def test_upload_by_missing_user_fails(self):
        self.assertIsNone(self.fs.file_upload_by("nope", "a", 1))

    def test_admin_upload_unlimited(self):
        self.fs.add_user("u1", 1)
        self.fs.file_upload("admin_file", 10_000)  # should still work
        self.assertEqual(self.fs.file_get("admin_file"), 10_000)

    def test_search_includes_all_users_files(self):
        self.fs.add_user("u1", 100)
        self.fs.add_user("u2", 100)
        self.fs.file_upload_by("u1", "aa", 5)
        self.fs.file_upload_by("u2", "ab", 7)
        self.assertEqual(self.fs.file_search("a"), ["ab(7)", "aa(5)"])
