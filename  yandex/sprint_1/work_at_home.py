def solution(n):
    result = ''
    if n == 0:
        return 0
    while n != 0:
        result = str(n % 2) + result
        n = n // 2
    return result


def main():
    s = int(input())
    result = solution(s)
    print(result)


if __name__ == '__main__':
    main()
