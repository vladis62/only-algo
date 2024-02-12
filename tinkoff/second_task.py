def second_task(strings):
    min_s = 999
    max_s = -1
    for s in strings:
        min_s = min(len(s), min_s)
        max_s = max(len(s), max_s)
    return [min_s, max_s]


def main():
    _ = input()
    strings = input().split('#')

    print(*second_task(strings))


if __name__ == '__main__':
    main()
