def solution(a, b):
    result = ''
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    if len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    remainder = 0
    for i in range(len(a) - 1, -1, -1):
        res = int(a[i]) + int(b[i]) + remainder
        if res > 9:
            remainder = 1
        else:
            remainder = 0
        result = str(res % 10) + result
    if remainder:
        result = str(remainder) + result
    return result.replace('', ' ').strip()


def main():
    _ = input()
    arr1 = input().replace(' ', '')
    arr2 = input()
    result = solution(arr1, arr2)
    print(result)


if __name__ == '__main__':
    main()
