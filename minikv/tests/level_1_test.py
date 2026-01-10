import unittest
from kv_store_impl import KVStoreImpl

class Level1Tests(unittest.TestCase):
    def setUp(self):
        self.kv = KVStoreImpl()

    def test_put_get(self):
        self.kv.put("a", "1")
        self.assertEqual(self.kv.get("a"), "1")

    def test_overwrite(self):
        self.kv.put("a", "1")
        self.kv.put("a", "2")
        self.assertEqual(self.kv.get("a"), "2")

    def test_delete(self):
        self.kv.put("a", "1")
        self.assertTrue(self.kv.delete("a"))
        self.assertIsNone(self.kv.get("a"))

    def test_delete_missing(self):
        self.assertFalse(self.kv.delete("missing"))

    def test_count(self):
        self.assertEqual(self.kv.count(), 0)
        self.kv.put("a", "1")
        self.kv.put("b", "2")
        self.assertEqual(self.kv.count(), 2)
        self.kv.delete("a")
        self.assertEqual(self.kv.count(), 1)
