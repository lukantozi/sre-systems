import unittest
from kv_store_impl import KVStoreImpl

class Level2Tests(unittest.TestCase):
    def setUp(self):
        self.kv = KVStoreImpl()

    def test_keys_empty(self):
        self.assertEqual(self.kv.keys("a"), [])
        self.assertEqual(self.kv.dump(), [])

    def test_keys_prefix(self):
        self.kv.put("app", "1")
        self.kv.put("apple", "2")
        self.kv.put("banana", "3")
        self.kv.put("apply", "4")

        self.assertEqual(self.kv.keys("app"), ["app", "apple", "apply"])
        self.assertEqual(self.kv.keys("ban"), ["banana"])
        self.assertEqual(self.kv.keys("x"), [])

    def test_dump_sorted(self):
        self.kv.put("b", "2")
        self.kv.put("a", "1")
        self.kv.put("c", "3")
        self.assertEqual(self.kv.dump(), [("a", "1"), ("b", "2"), ("c", "3")])

    def test_delete_affects_queries(self):
        self.kv.put("aa", "1")
        self.kv.put("ab", "2")
        self.kv.put("b", "3")
        self.assertTrue(self.kv.delete("ab"))

        self.assertEqual(self.kv.keys("a"), ["aa"])
        self.assertEqual(self.kv.dump(), [("aa", "1"), ("b", "3")])

    def test_overwrite_updates_dump(self):
        self.kv.put("k", "v1")
        self.kv.put("k", "v2")
        self.assertEqual(self.kv.dump(), [("k", "v2")])

