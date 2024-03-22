class Solution(object):
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        merged_intervals = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            merged_intervals.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        merged_intervals.append(newInterval)

        while i < n:
            merged_intervals.append(intervals[i])
            i += 1

        return merged_intervals


print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
