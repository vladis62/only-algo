class Solution(object):
    def maxDistToClosest(self, seats):
        cur, cur_max = 0, 0
        left = 0
        right = 0
        while seats[left] == 0:
            left += 1

        while seats[len(seats) - right - 1] == 0:
            right += 1

        for seat in seats:
            if seat == 0:
                cur += 1
                cur_max = max(cur_max, cur)
            else:
                cur = 0

        return max(left, right, (cur_max + 1) // 2)


def main():
    print(Solution().maxDistToClosest([1, 1, 0, 0, 0, 1, 0]))


if __name__ == '__main__':
    main()
