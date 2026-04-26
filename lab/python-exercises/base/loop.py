def loop(n):
    """
    Input: 5 → Output: 15   # 1+2+3+4+5
    Input: 0 → Output: 0
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(loop(5))
print(loop(0))
