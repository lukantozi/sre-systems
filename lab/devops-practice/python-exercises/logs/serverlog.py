class ServerLog:
    
    def __init__(self, server_name):
        self.server_name = server_name
        self.entries = []

    def add_entry(self, level, message):
        if level in {"INFO", "ERROR", "WARN"}:
            self.entries.append({"level": level, "message": message})
        else:
            raise ValueError(f"Unkown level: {level}\nValid levels: INFO | ERROR | WARN")

    def get_errors(self):
        return [entry["message"] for entry in self.entries if entry["level"] == "ERROR"]

    def __str__(self):
        return f"ServerLog[{self.server_name}]: {len(self.entries)} entries"


log = ServerLog("web-01")
log.add_entry("INFO", "started")
log.add_entry("ERROR", "disk full")
log.add_entry("WARN", "high cpu")
log.add_entry("ERROR", "oom kill")
print(log)
print(log.get_errors())

