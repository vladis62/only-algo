def subsequence(s1, s2):
    i, j = 0, 0

    l1, l2 = len(s1), len(s2)
    while i < l1 and j < l2:
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return l1 == i


def main():
    s1 = input()
    s2 = input()
    print(subsequence(s1, s2))


if __name__ == '__main__':
    main()
