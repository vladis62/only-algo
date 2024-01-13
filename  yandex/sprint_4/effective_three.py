def effective_tree(nums, x):
    result = set()
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum > x:
                r -= 1
            elif three_sum < x:
                l += 1
            else:
                result.add((a, nums[l], nums[r]))
                l += 1
                while nums[i] == nums[i - 1] and l < r:
                    l += 1
    return result


def main():
    arr = [6, 6, 4, 4, 0, 8, 10]
    fours = effective_tree(arr, 16)
    print(len(fours))
    [print(*four) for four in fours]


if __name__ == '__main__':
    main()
