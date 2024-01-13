class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


def main():
    arr = [2, 1, 4, 3, 12]
    Solution().moveZeroes(arr)
    print(arr)


if __name__ == '__main__':
    main()
