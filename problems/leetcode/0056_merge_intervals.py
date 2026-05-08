class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ptr = 0
        while ptr < len(intervals)-1:
            if intervals[ptr][1] >= intervals[ptr+1][0] and intervals[ptr][1] <= intervals[ptr+1][1]:
                intervals[ptr][1] = intervals[ptr+1][1]
                intervals.pop(ptr+1)
            elif intervals[ptr][1] > intervals[ptr+1][1]:
                intervals.pop(ptr+1)
            else:
                ptr += 1
        return intervals
            


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[4,7],[1,4]]))
print(Solution().merge([[1,4],[2,3]]))
print(Solution().merge([[1,4],[0,2],[3,5]]))


# O(n)
class Solution:
    def merge_On(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start, prev_end = res[-1]
            
            if start <= prev_end:
                updated_end = max(prev_end, end)
                res.pop()
                res.append([prev_start, updated_end])
            else:
                res.append([start, end])
        
        return res
