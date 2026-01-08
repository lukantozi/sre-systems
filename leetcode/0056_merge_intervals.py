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
