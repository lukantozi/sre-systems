import unittest
from kv_store_impl import KVStoreImpl

class Level4Tests(unittest.TestCase):
    def setUp(self):
        self.kv = KVStoreImpl()

    def test_rollback_removes_future_writes(self):
        self.kv.put_at("a", "1", ts=10)
        self.kv.put_at("a", "2", ts=20)
        self.kv.rollback(10)

        self.assertEqual(self.kv.get_at("a", ts=10), "1")
        self.assertEqual(self.kv.get_at("a", ts=15), "1")
        self.assertEqual(self.kv.get_at("a", ts=25), "1")

    def test_rollback_restores_deleted_key(self):
        self.kv.put_at("a", "1", ts=10)
        self.kv.delete_at("a", ts=20)
        self.kv.rollback(15)

        self.assertEqual(self.kv.get_at("a", ts=15), "1")
        self.assertEqual(self.kv.get_at("a", ts=25), "1")

    def test_rollback_drops_delete(self):
        self.kv.put_at("a", "1", ts=10)
        self.kv.delete_at("a", ts=20)
        self.kv.rollback(25)

        self.assertIsNone(self.kv.get_at("a", ts=25))

    def test_rollback_with_ttl(self):
        self.kv.put_at("a", "1", ts=10, ttl=10)  # alive [10,20)
        self.kv.put_at("a", "2", ts=15, ttl=100)
        self.kv.rollback(12)

        self.assertEqual(self.kv.get_at("a", ts=19), "1")
        self.assertIsNone(self.kv.get_at("a", ts=20))
