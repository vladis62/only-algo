def twoSum(self, nums, target):
    num_to_index = {}
    for i in range(len(nums)):
        if target - nums[i] in num_to_index:
            return [num_to_index[target - nums[i]], i]
        num_to_index[nums[i]] = i
    return []


if __name__ == '__main__':
    print(twoSum('PyCharm', [2, 7, 11, 15], 9))
