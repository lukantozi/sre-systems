import argparse
import json
from os import walk, path


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default="/", help="dir to scan. Default: '/'")
    parser.add_argument("--min-size", default="10MB", help="Filter threshold (e.g. 1MB)")
    parser.add_argument("--output", default="tmp.json", help="output JSON file path")

    args = parser.parse_args()
    return args


def parse_size(sib):
    letter_found = False
    ind = 0
    for char in sib:
        if char.isdigit():
            if not letter_found:
                ind += 1
            else:
                raise ValueError("Wrong format. Examples: [ 100MB | 20B ]")
        else:
            letter_found = True

    upscale = {"B": 1, "KB": 10**3, "MB": 10**6, "GB": 10**9}
    number = int(sib[:ind])
    unit = sib[ind:]

    if unit not in {"B", "KB", "MB", "GB"}:
        raise ValueError("Wrong size unit. Valid: [ B | KB | MB | GB ]")
    return number * upscale[unit]


def walk_disk(in_path, size):
    to_write = []

    for dirpath, _, files in walk(in_path):
        try:
            if path.getsize(dirpath) >= size:
                size_mb = round(path.getsize(dirpath) / 10**6, 2)
                to_write.append({"path": dirpath, "size_mb": size_mb})
        except (PermissionError, OSError):
            continue

        if files:
            for file in files:
                filepath = path.join(dirpath, file)
                try:
                    if path.exists(filepath) and path.getsize(filepath) >= size:
                        size_mb = round(path.getsize(filepath) / 10**6, 2)
                        to_write.append({"path": filepath, "size_mb": size_mb})
                except (PermissionError, OSError):
                    continue
    return to_write


def write_json(data, out):
    with open(out, "w") as f:
        f.write(json.dumps(data))


def main():
    args = parse_arguments()
    in_path = args.path
    size = parse_size(args.min_size)
    json_output = args.output

    filtered = walk_disk(in_path, size)
    filtered.sort(key=lambda x: x["size_mb"], reverse=True)

    write_json(filtered, json_output)


if __name__ == "__main__":
    main()
