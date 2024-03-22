def insert_strs(main_str, inner_strs):
    n = len(inner_strs)
    result = ''

    pre_idx = -1
    last_idx = inner_strs[-1][1]
    for i in range(n):
        inner_str, index = inner_strs[i]
        if index == 0:
            result = inner_str + result
            continue

        if pre_idx == -1:
            result += main_str[0:index] + inner_str
            pre_idx = index
        else:
            result += main_str[pre_idx:index] + inner_str
            pre_idx = index

    if last_idx < len(main_str):
        result += main_str[last_idx:]

    return result


def main():
    string = input()
    n = int(input())
    actions = []

    for _ in range(n):
        inner_str, idx = list(map(str, input().split()))
        actions.append((inner_str, int(idx)))

    inner_strs = sorted(actions, key=lambda x: x[1])

    print(insert_strs(string, inner_strs))


if __name__ == '__main__':
    main()

