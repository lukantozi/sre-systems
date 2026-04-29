class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        hash_s1 = {}
        for l in s1:
            if l not in hash_s1:
                hash_s1[l] = 1
            else:
                hash_s1[l] += 1

        hash_s2 = {}
        l = None
        for i in range(len(s2)):
            for j in range(len(s1)):
                try:
                    l = s2[i+j]
                except IndexError:
                    return False
                if l not in hash_s2:
                    hash_s2[l] = 1
                else:
                    hash_s2[l] += 1
            if hash_s1 == hash_s2:
                return True
            hash_s2.clear()
        return False

print(Solution().checkInclusion("ab", "eidbaooo")) # -> true
print(Solution().checkInclusion("ab", "eidboaoo")) # -> false
