def evens(n):
    """
    Input: 3426 → Output: 2   # 4 and 2 are even
    Input: 111  → Output: 0
    """
    count = 0
    while n != 0:
        if (n % 10) % 2 == 0: count += 1
        n //= 10
    return count

print(evens(3426))
print(evens(111))
print(evens(222))
