import heapq


# https://leetcode.com/problems/furthest-building-you-can-reach

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        diffs = []
        n = len(heights)

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(diffs, diff)
                if len(diffs) > ladders:
                    bricks -= heapq.heappop(diffs)
                if bricks < 0:
                    return i

        return len(heights) - 1


def main():
    print(Solution().furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))


if __name__ == '__main__':
    main()
