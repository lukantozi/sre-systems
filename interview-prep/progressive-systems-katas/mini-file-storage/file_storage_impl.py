from file_storage import FileStorage

class FileStorageImpl(FileStorage):
    def __init__(self):
        self.storage = {}
        self.users = {}
        self.backup = {}

    def file_upload(self, file_name: str, size_bytes: int) -> None:
        if file_name not in self.storage:
            self.storage[file_name] = size_bytes
        else:
            raise RuntimeError

    def file_get(self, file_name: str) -> int | None:
        if file_name not in self.storage:
            return None
        return self.storage[file_name]

    def file_copy(self, source: str, dest: str) -> None:
        if source not in self.storage:
            raise RuntimeError
        self.storage[dest] = self.storage[source]
        return None

    def file_search(self, prefix: str) -> list[str]:
        matches = []
        for file in self.storage:
            if file.startswith(prefix):
                matches.append((file, self.storage[file]))

        matches.sort(key=lambda t: (-t[1], t[0]))
        matches_formatted = [f"{match[0]}({match[1]})" for match in matches[:10]]
        return matches_formatted

    def add_user(self, user_id: str, capacity: int) -> bool:
        if user_id in self.users:
            return False
        self.users[user_id] = [capacity, capacity, {}]
        return True

    def file_upload_by(self, user_id: str, file_name: str, size_bytes: int) -> int | None:
        if user_id not in self.users:
            return None
        if file_name in self.storage:
            return None
        if self.users[user_id][1] - size_bytes < 0:
            return None

        self.users[user_id][2][file_name] = size_bytes
        self.storage[file_name] = size_bytes
        self.users[user_id][1] -= size_bytes
        return self.users[user_id][1]

    def backup_user(self, user_id: str) -> int | None:
        if user_id not in self.users:
            return None
        self.backup[user_id] = self.users[user_id][2].copy()
        return len(self.backup[user_id])


    def restore_user(self, user_id: str) -> int | None:
        if user_id not in self.users or user_id not in self.backup:
            return None

        # remove user's current files from global storage
        for fname in list(self.users[user_id][2].keys()):
            self.storage.pop(fname, None)

        # restore user's files dict from snapshot
        self.users[user_id][2] = self.backup[user_id].copy()

        # put restored files back into global storage
        for fname, size in self.users[user_id][2].items():
            self.storage[fname] = size

        # recompute remaining
        used = sum(self.users[user_id][2].values())   # sum dict values [web:1089]
        total = self.users[user_id][0]
        self.users[user_id][1] = total - used
        return len(self.users[user_id][2])
