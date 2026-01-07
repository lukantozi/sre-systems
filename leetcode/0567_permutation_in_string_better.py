class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_hash, s2_hash = [0]*26, [0]*26

        for i in range(len(s1)):
            s1_hash[ord(s1[i])-(ord('a'))] += 1 
            s2_hash[ord(s2[i])-(ord('a'))] += 1 

        if s1_hash == s2_hash:
            return True

        l, r = 0, len(s1)
        while r < len(s2):
            s2_hash[ord(s2[r])-(ord('a'))] += 1 
            s2_hash[ord(s2[l])-(ord('a'))] -= 1 
            if s1_hash == s2_hash:
                return True
            r += 1
            l += 1

        return False

print(Solution().checkInclusion("ab", "eidbaooo")) # -> true
print(Solution().checkInclusion("ab", "eidboaoo")) # -> false
