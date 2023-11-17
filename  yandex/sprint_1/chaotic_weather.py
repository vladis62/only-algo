def solution(arr, n):
    count = 0
    if n == 1:
        return 1
    for i in range(0, n):
        if (i - 1 < 0 or arr[i] > arr[i - 1]) and (i + 1 == n or arr[i] > arr[i + 1]):
            count += 1
    return count


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = solution(arr, n)
    print(result)


if __name__ == '__main__':
    main()
