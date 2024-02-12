def count_trees(n):
    if n == 0 or n == 1:
        return 1

    total = 0
    for i in range(1, n + 1):
        left_subtrees = count_trees(i - 1)
        right_subtrees = count_trees(n - i)
        total += left_subtrees * right_subtrees

    return total


def main():
    n = int(input())
    print(count_trees(n))


if __name__ == '__main__':
    main()
