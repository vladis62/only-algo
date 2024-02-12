def second(data):
    history = set()
    result = []
    for v in data:
        test1 = str(int(v[0]) + 1) + v[1]
        test2 = str(int(v[0]) - 1) + v[1]
        if test1 in history or test2 in history:
            continue
        k_v = v[0] + v[1]
        history.add(k_v)
        result.append([v[0], v[1]])
    return result


def main():
    n, m = list(map(int, input().split()))
    data_list = []

    for _ in range(m):
        line = list(map(str, input().split()))
        timestamp = line[0]
        value = line[1]
        data_list.append([timestamp, value])

    res = second(data_list)
    for r in res:
        print(*r)


if __name__ == '__main__':
    main()
