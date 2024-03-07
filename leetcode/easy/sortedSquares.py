class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                nums[i] = nums[i] ** 2
        while True:
            if nums[0] < 0:
                nums[0] = nums[0] ** 2
                i = 0
                for j in range(1, n):
                    if nums[i] > nums[j] or nums[j] < 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                    else:
                        break
            else:
                break
        return nums


def main():
    print(Solution().sortedSquares([-4, -1, 0, 3, 10]))


if __name__ == '__main__':
    main()
