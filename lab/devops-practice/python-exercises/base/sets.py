def set_dif(s1, s2):
    """
    Input: [4, 1, 2, 1, 3], [3, 5, 2, 6]
    Output: [2, 3]
    """
    new_set = set(s1) & set(s2)
    return sorted(new_set)

print(set_dif([4, 1, 2, 1, 3], [3, 5, 2, 6]))

