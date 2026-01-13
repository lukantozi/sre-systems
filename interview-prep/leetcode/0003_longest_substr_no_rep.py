class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)
        return best


solution = Solution()
#print(solution.lengthOfLongestSubstring("abcabcbb")) # -> 3 "abc", "bca", "cab"
#print(solution.lengthOfLongestSubstring("bbbbb")) # -> 1 "b"
#print(solution.lengthOfLongestSubstring("pwwkew")) # -> 3 "wke"
#print(solution.lengthOfLongestSubstring(" ")) # -> 1
#print(solution.lengthOfLongestSubstring("ua ")) # -> 3
#print(solution.lengthOfLongestSubstring("aab")) # -> 2
#print(solution.lengthOfLongestSubstring("cdd")) # -> 2
print(solution.lengthOfLongestSubstring("dvdf")) # -> 3
with open("test_case_987", "r") as file:
    test_case = file.read()

print(solution.lengthOfLongestSubstring(test_case)) # -> 3
