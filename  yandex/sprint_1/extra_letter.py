def solution(a, b):
    s = {}
    for c in a:
        if s.get(c) is None:
            s[c] = 1
        else:
            s[c] = s[c] + 1
    for c in b:
        if s.get(c) == 0 or s.get(c) is None:
            return c
        s[c] = s[c] - 1
    if len(s) != 0:
        return list(s.keys())[0]


def main():
    a = input()
    b = input()
    result = solution(a, b)
    print(result)


if __name__ == '__main__':
    main()
