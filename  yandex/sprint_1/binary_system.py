def solution(a, b):
    result = ''
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    if len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    remainder = 0
    for i in range(len(a) - 1, -1, -1):
        res = int(a[i]) + int(b[i]) + remainder
        if res > 2:
            remainder = 1
            result = '1' + result
        elif res > 1:
            remainder = 1
            result = '0' + result
        else:
            remainder = 0
            result = str(res) + result
    if remainder == 1:
        result = '1' + result
    return result


def main():
    a = input()
    b = input()
    result = solution(a, b)
    print(result)


if __name__ == '__main__':
    main()
