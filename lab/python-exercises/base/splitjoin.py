def joined_by(l):
    """
    Input: ["cat", "docker", "is", "linux", "ok"]
    Output: "docker | linux"
    """
    joined = " | ".join([word for word in l if len(word) > 3])
    return joined

print(joined_by(["cat", "docker", "is", "linux", "ok"]))
