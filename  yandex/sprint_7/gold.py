def gold_backpack(capacity, golds):
    golds = sorted(golds, key=lambda x: -x[0])
    backpack = 0

    for gold, weight in golds:
        if capacity >= weight:
            backpack += (gold * weight)
            capacity -= weight
        else:
            backpack += (gold * capacity)
            break
        if capacity == 0:
            break
    return backpack


def main():
    capacity = int(input())
    n = int(input())
    golds = [list(map(int, input().split())) for _ in range(n)]
    backpack = gold_backpack(capacity, golds)
    print(backpack)


if __name__ == '__main__':
    main()
