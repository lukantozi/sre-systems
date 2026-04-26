def word_freq(s):
    """
    Input: "the cat sat on the mat"
    Output: {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
    """
    freq = {}
    words = s.split()
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_freq("the cat sat on the mat"))
