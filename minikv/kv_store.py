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
