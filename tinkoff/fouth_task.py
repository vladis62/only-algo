def fourth_task(nums):
    nums = sorted(set(nums))

    result = []
    start = end = nums[0]

    for number in nums[1:]:
        if number == end + 1:
            end = number
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(start)
                if end - start > 1:
                    result.append('...')
                result.append(end)
            start = end = number

    if start == end:
        result.append(str(start))
    else:
        result.append(start)
        if end - start > 1:
            result.append('...')
        result.append(end)

    return result


def main():
    _ = input()
    nums = list(map(int, input().split()))
    print(*fourth_task(nums))


if __name__ == '__main__':
    main()
