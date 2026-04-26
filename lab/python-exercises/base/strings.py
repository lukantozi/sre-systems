def palindrome(s):
    """
    Input: "Racecar" → True
    Input: "docker"  → False
    """
    st = s.lower()
    if st == st[::-1]: return True
    return False

print(palindrome("Racecar"))
print(palindrome("docker"))
