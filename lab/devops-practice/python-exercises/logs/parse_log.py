from collections import defaultdict

def parse_log_file(filepath):
    parsed_logs = defaultdict(list)
    try:
        with open(filepath, "r") as f:
            for line in f:
                line_split = line.strip().split(":", 1)
                level = line_split[0]
                if level in {"INFO", "ERROR", "WARN"}:
                    message = line_split[1]
                    parsed_logs[level].append(message)
    except FileNotFoundError:
        print(f"Warning: {filepath} not found")
        return {}

    return dict(parsed_logs)

print(parse_log_file("log.txt"))
