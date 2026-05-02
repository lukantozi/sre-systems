def running_total(l):
    """
    Input: [1, 2, 3, 4]
    Output: [1, 3, 6, 10]
    """
    new_list = []
    tot = 0
    for i in l:
        tot += i
        new_list.append(tot)
    return new_list

print(running_total([1,2,3,4]))
