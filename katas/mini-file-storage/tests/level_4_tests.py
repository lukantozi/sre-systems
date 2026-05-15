import unittest
from file_storage_impl import FileStorageImpl

class Level4Tests(unittest.TestCase):
    def setUp(self):
        self.fs = FileStorageImpl()
        self.fs.add_user("u1", 10_000)
        self.fs.add_user("u2", 10_000)

    def test_backup_missing_user(self):
        self.assertIsNone(self.fs.backup_user("nope"))

    def test_restore_missing_user(self):
        self.assertIsNone(self.fs.restore_user("nope"))

    def test_restore_without_backup_fails(self):
        self.assertIsNone(self.fs.restore_user("u1"))

    def test_backup_and_restore_exact_state(self):
        self.fs.file_upload_by("u1", "a", 5)
        self.fs.file_upload_by("u1", "b", 7)
        self.assertEqual(self.fs.backup_user("u1"), 2)

        # mutate after backup
        self.fs.file_upload_by("u1", "c", 9)
        self.fs.file_copy("a", "admin_copy_of_a")  # admin file should not be affected

        # restore should revert u1 to {a,b} only
        self.assertEqual(self.fs.restore_user("u1"), 2)
        self.assertEqual(self.fs.file_get("a"), 5)
        self.assertEqual(self.fs.file_get("b"), 7)
        self.assertIsNone(self.fs.file_get("c"))
        self.assertEqual(self.fs.file_get("admin_copy_of_a"), 5)

    def test_backup_overwrite(self):
        self.fs.file_upload_by("u2", "x", 1)
        self.assertEqual(self.fs.backup_user("u2"), 1)
        self.fs.file_upload_by("u2", "y", 2)
        self.assertEqual(self.fs.backup_user("u2"), 2)  # overwrite backup with new state

        self.fs.file_upload_by("u2", "z", 3)  # extra file after backup
        self.assertEqual(self.fs.restore_user("u2"), 2)
        self.assertIsNone(self.fs.file_get("z"))
        self.assertEqual(self.fs.file_search(""), ["y(2)", "x(1)"][:10])  # depends on your search prefix rules
