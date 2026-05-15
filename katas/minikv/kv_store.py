from abc import ABC

class KVStore(ABC):
    def put(self, key: str, value: str) -> None:
        return None

    def get(self, key: str) -> str | None:
        return None

    def delete(self, key: str) -> bool:
        return False

    def count(self) -> int:
        return 0

    def keys(self, prefix: str) -> list[str]:
        return []

    def dump(self) -> list[tuple[str, str]]:
        return []

    def put_at(self, key: str, value: str, ts: int, ttl: int | None = None) -> None:
        return None

    def get_at(self, key: str, ts: int) -> str | None:
        return None

    def delete_at(self, key: str, ts: int) -> bool:
        return False

    def count_at(self, ts: int) -> int:
        return 0

    def keys_at(self, prefix: str, ts: int) -> list[str]:
        return []

    def dump_at(self, ts: int) -> list[tuple[str, str]]:
        return []

    def rollback(self, ts: int) -> None:
        return None
