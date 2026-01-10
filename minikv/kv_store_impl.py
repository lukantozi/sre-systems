from kv_store import KVStore

class KVStoreImpl(KVStore):
    def __init__(self):
        self.table = {}

    def put(self, key: str, value: str) -> None:
        self.table[key] = value

    def get(self, key: str) -> str | None:
        if key in self.table:
            return self.table[key]
        else:
            return None

    def delete(self, key: str) -> bool:
        if key in self.table:
            self.table.pop(key)
            return True
        return False

    def count(self) -> int:
        return len(self.table)
