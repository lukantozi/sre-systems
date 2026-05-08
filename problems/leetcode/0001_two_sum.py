class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 0
        for num_1 in nums:
            j = i + 1
            for num_2 in nums[j:]:
                if num_1 + num_2 == target:
                    return [i, j]
                j += 1
            i += 1

solution = Solution()
print(solution.twoSum([3,2,4], 6))

# O(n)
class Solution(object):
    def twoSum_On(self, nums, target):
        seen = {}  # value -> index
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
