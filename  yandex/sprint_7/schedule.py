def schedule(times):
    times = sorted(times, key=lambda x: (x[1], x[0]))
    result = [times[0]]
    for i in range(1, len(times)):
        if result[-1][1] <= times[i][0]:
            result.append(times[i])
    return result


def main():
    n = int(input())
    times = [list(map(float, input().split())) for _ in range(n)]
    result = schedule(times)
    print(len(result))
    for res in result:
        print(*(int(x) if x.is_integer() else x for x in res))


if __name__ == '__main__':
    main()


# 7
# 19 19
# 12 14
# 7 14
# 8 22
# 22 23
# 5 21
# 9 23
