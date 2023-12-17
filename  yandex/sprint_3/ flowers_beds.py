def flowers_beds(arr):
    result = []
    for i in range(len(arr)):
        if not result:
            result.append(arr[i])
        elif arr[i][0] <= result[-1][1] < arr[i][1]:
            result[-1][1] = arr[i][1]
        elif not (arr[i][0] <= result[-1][1] >= arr[i][1]):
            result.append(arr[i])
    return result


def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = sorted(arr)
    for e in flowers_beds(res):
        print(*e)


if __name__ == '__main__':
    main()
