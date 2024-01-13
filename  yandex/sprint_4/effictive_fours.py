def effective_four(nums, x):
    nums.sort()
    result = set()

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left = j + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == x:
                    result.add((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif current_sum < x:
                    left += 1
                else:
                    right -= 1

    return sorted(list(result))


def main():
    _ = int(input())
    x = int(input())
    arr = list(map(int, input().split()))
    fours = effective_four(arr, x)
    print(len(fours))
    [print(*four) for four in fours]


if __name__ == '__main__':
    main()
