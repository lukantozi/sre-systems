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

        for i in range(0, len(s2), len(s1)):
            hash_s2 = {}
            for l in s2[i:len(s1)]:
                if l not in hash_s2:
                    hash_s2[l] = 1
                else:
                    hash_s1[l] += 1
        return True

#print(Solution().checkInclusion("ab", "eidbaooo")) # -> true
#print(Solution().checkInclusion("ab", "eidboaoo")) # -> false
hash = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

s1 = "ab"
hash_s1 = {}
for l in s1:
    if l not in hash_s1:
        hash_s1[l] = 1
    else:
        hash_s1[l] += 1
print(hash_s1)

s2 = "eidboaoo"

hash_s2 = {}
for i in range(len(s2)):
    for l in s2[i:len(s1)+1]:
        print(l)
        if l not in hash_s2:
            hash_s2[l] = 1
        else:
            hash_s2[l] += 1
print(hash_s2)
