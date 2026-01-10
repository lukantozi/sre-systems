import unittest
from kv_store_impl import KVStoreImpl

class Level3Tests(unittest.TestCase):
    def setUp(self):
        self.kv = KVStoreImpl()

    def test_put_at_get_at_no_ttl(self):
        self.kv.put_at("a", "1", ts=10)
        self.assertIsNone(self.kv.get_at("a", ts=9))
        self.assertEqual(self.kv.get_at("a", ts=10), "1")
        self.assertEqual(self.kv.get_at("a", ts=999), "1")

    def test_ttl_expiration(self):
        self.kv.put_at("a", "1", ts=10, ttl=5)  # alive for t in [10, 15)
        self.assertEqual(self.kv.get_at("a", ts=10), "1")
        self.assertEqual(self.kv.get_at("a", ts=14), "1")
        self.assertIsNone(self.kv.get_at("a", ts=15))
        self.assertIsNone(self.kv.get_at("a", ts=100))

    def test_overwrite_resets_ttl(self):
        self.kv.put_at("a", "1", ts=10, ttl=5)   # expires at 15
        self.kv.put_at("a", "2", ts=14, ttl=10)  # expires at 24
        self.assertEqual(self.kv.get_at("a", ts=14), "2")
        self.assertEqual(self.kv.get_at("a", ts=15), "2")  # old would be expired here
        self.assertIsNone(self.kv.get_at("a", ts=24))

    def test_delete_at(self):
        self.kv.put_at("a", "1", ts=10, ttl=100)
        self.assertFalse(self.kv.delete_at("missing", ts=10))
        self.assertTrue(self.kv.delete_at("a", ts=50))
        self.assertIsNone(self.kv.get_at("a", ts=50))
        self.assertFalse(self.kv.delete_at("a", ts=60))

    def test_count_at(self):
        self.kv.put_at("a", "1", ts=10, ttl=5)    # alive until 15
        self.kv.put_at("b", "2", ts=12)           # forever
        self.kv.put_at("c", "3", ts=20, ttl=2)    # alive until 22

        self.assertEqual(self.kv.count_at(9), 0)
        self.assertEqual(self.kv.count_at(10), 1)   # a
        self.assertEqual(self.kv.count_at(14), 2)   # a,b
        self.assertEqual(self.kv.count_at(15), 1)   # b
        self.assertEqual(self.kv.count_at(21), 2)   # b,c
        self.assertEqual(self.kv.count_at(22), 1)   # b

    def test_keys_at_and_dump_at(self):
        self.kv.put_at("app", "1", ts=10, ttl=5)     # alive until 15
        self.kv.put_at("apple", "2", ts=10)          # forever
        self.kv.put_at("banana", "3", ts=12, ttl=1)  # alive until 13

        self.assertEqual(self.kv.keys_at("app", ts=11), ["app", "apple"])
        self.assertEqual(self.kv.dump_at(ts=11), [("app", "1"), ("apple", "2")])

        self.assertEqual(self.kv.keys_at("b", ts=12), ["banana"])
        self.assertEqual(self.kv.keys_at("b", ts=13), [])  # banana expired at 13

        self.assertEqual(self.kv.dump_at(ts=16), [("apple", "2")])  # app expired at 15
