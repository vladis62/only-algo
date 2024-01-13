class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [i, hash[target - nums[i]]]
            hash[nums[i]] = i
        return -1


def main():
    print(Solution().twoSum([3, 2, 4], 6))


if __name__ == '__main__':
    main()
