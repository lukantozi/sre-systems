class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]):# -> int
        intervals.sort(key=lambda a: a[1])
        removals = 0
        end = intervals[0][1]

        for start, finish in intervals[1:]:
            if start < end:
                removals += 1
            else:
                end = finish
        return removals


print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(Solution().eraseOverlapIntervals([[1,2],[2,3]]))
print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))
print(Solution().eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
print(Solution().eraseOverlapIntervals([[1,2],[1,3],[1,4]]))
print(Solution().eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))
