def main():
    n = int(input())
    prefix = input()

    for _ in range(n - 1):
        line = input()
        min_len = min(len(prefix), len(line))
        j = 0
        while j < min_len and prefix[j] == line[j]:
            j += 1
        prefix = line[:j]

    print(len(prefix))


if __name__ == "__main__":
    main()
