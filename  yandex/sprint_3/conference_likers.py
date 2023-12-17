from collections import Counter


def solution(ids, n):
    ids.sort()
    id_counts = Counter(ids)
    result = [id for id, _ in id_counts.most_common(n)]
    return result


def main():
    _ = input()
    ids = list(map(int, input().split(' ')))
    n = int(input())
    print(*solution(ids, n))


if __name__ == '__main__':
    main()
