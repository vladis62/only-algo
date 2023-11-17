def solution(n):
    result = 4
    if n == 1:
        return True
    while result <= n:
        if result == n:
            return True
        result *= 4
    return False


def main():
    n = int(input())
    result = solution(n)
    print(result)


if __name__ == '__main__':
    main()
