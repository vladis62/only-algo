def max_substring(s):
    history = set()
    cur_len, max_len = 0, 0
    l, r = 0, 0
    while r < len(s):
        if s[r] not in history:
            cur_len += 1
            history.add(s[r])
            r += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 0
            l += 1
            r = l
            history.clear()
    return max(max_len, len(history))


def main():
    s = input()
    print(max_substring(s))


if __name__ == '__main__':
    main()
