def parse():
    loaded = []
    with open("sample.log", "r") as f:
        lines = f.readlines()
    for n, line in enumerate(lines):
        line = line.split(" ")
        # TODO: make real validation
        if len(line) < 4: 
            continue
        tmst = line[0] + " " + line[1]
        lvl = line[2]
        msg = " ".join(line[3:]).strip()
        loaded.append({
            "timestamp": tmst,
            "level": lvl,
            "message": msg,
            })
    return loaded


if __name__ == "__main__":
    import pprint
    l = parse()
    pprint.pprint(l, sort_dicts=False)
