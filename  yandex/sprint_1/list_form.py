def solution(arr1, arr2):
    result = ''
    max_arr = min(len(arr1), len(arr2))
    sum_arr = ''
    carry = 0
    j = 0
    for i in range(0, max_arr):
        s = arr1[i] + arr2[i] + carry
        if s > 9:
            carry = 1
        else:
            carry = 0
        sum_arr = str(s) + sum_arr
        j = i
    if carry:
        sum_arr = str(s) + sum_arr
    return result


def main():
    _ = input()
    arr1 = list(map(int, input().split()))
    arr2 = [int(digit) for digit in str(input())]
    result = solution(arr1, arr2)
    print(result)


if __name__ == '__main__':
    main()
