from kv_store import KVStore

class KVStoreImpl(KVStore):
    def __init__(self):
        self.table = {}
        self.log = []

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

    def keys(self, prefix: str) -> list[str]:
        keys_pref = []
        for k in self.table:
            if k.startswith(prefix):
                keys_pref.append(k)
        keys_pref.sort()
        return keys_pref

    def dump(self) -> list[tuple[str, str]]:
        sorted_table = list(sorted(self.table.items()))
        return sorted_table

    def put_at(self, key: str, value: str, ts: int, ttl: int | None = None) -> None:
        self.table[key] = (value, ts, ttl)
        self.log.append(("put", ts, key, value, ttl))
        return None

    def get_at(self, key: str, ts: int) -> str | None:
        if key not in self.table:
            return None

        value, write_ts, ttl = self.table[key]
        if ts < write_ts:
            return None

        if ttl is None:
            return value

        if ts < write_ts + ttl:
            return value

        return None

    def delete_at(self, key: str, ts: int) -> bool:
        if self.get_at(key, ts) is None: 
            return False
        value, _, ttl = self.table[key]
        self.log.append(("del", ts, key))
        self.table.pop(key)
        return True

    def count_at(self, ts: int) -> int:
        count = 0
        for key in self.table: 
            if self.get_at(key, ts) is not None:
                count += 1
        return count

    def keys_at(self, prefix: str, ts: int) -> list[str]:
        keys_alive = []
        for key in self.table:
            if key.startswith(prefix):
                if self.get_at(key, ts) is not None:
                    keys_alive.append(key)
        keys_alive.sort()
        return keys_alive

    def dump_at(self, ts: int) -> list[tuple[str, str]]:
        key_value = []
        for key in self.table:
            val = self.get_at(key, ts)
            if val is not None:
                key_value.append((key, val))
        return key_value

    def rollback(self, ts: int) -> None:
        keep = [l for l in self.log if l[1] <= ts]
        self.table.clear()
        for log in keep:
            if ts >= log[1]:
                oper = log
                if oper[0] == "put":
                    _, ev_ts, key, value, ttl = oper
                    self.table[key] = (value, ev_ts, ttl)
                elif oper[0] == "del":
                    _, ev_ts, key = oper
                    self.table.pop(key, None)
        self.log = keep

        
        return None
