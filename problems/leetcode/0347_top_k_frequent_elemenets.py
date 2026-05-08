class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}
        seen_list = []
        for right, ch in enumerate(nums):
            seen[ch] = seen.get(nums[right], 0) + 1
        while k > 0:
            maxf = max(seen, key=lambda k: seen[k])
            seen_list.append(maxf)
            seen.pop(maxf)
            k -= 1
        return seen_list

#print(Solution().topKFrequent([1,1,1,2,2,3], 2))
print(Solution().topKFrequent([1], 1))
#print(Solution().topKFrequent([], 1))

# better
class Solution:
    def topKFrequent_better(self, nums: list[int], k: int) -> list[int]:
        fqs = {}
        k_fq = []

        for n in nums:
            fqs[n] = fqs.get(n, 0) + 1

        k_fq = sorted(fqs, key=fqs.get, reverse=True)[:k]
        
        return k_fq
