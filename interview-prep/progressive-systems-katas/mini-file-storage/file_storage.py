from abc import ABC

class FileStorage(ABC):
    def file_upload(self, file_name: str, size_bytes: int) -> None:
        return None

    def file_get(self, file_name: str) -> int | None:
        return None

    def file_copy(self, source: str, dest: str) -> None:
        return None

    def file_search(self, prefix: str) -> list[str]:
        return []

    def add_user(self, user_id: str, capacity: int) -> bool:
        return False

    def file_upload_by(self, user_id: str, file_name: str, size_bytes: int) -> int | None:
        return None

    def backup_user(self, user_id: str) -> int | None:
        return None

    def restore_user(self, user_id: str) -> int | None:
        return None

