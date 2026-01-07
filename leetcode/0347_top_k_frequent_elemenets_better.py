class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        fqs = {}
        k_fq = []

        for n in nums:
            fqs[n] = fqs.get(n, 0) + 1

        k_fq = sorted(fqs, key=fqs.get, reverse=True)[:k]
        
        return k_fq



print(Solution().topKFrequent([1,1,1,2,2,3], 2))
