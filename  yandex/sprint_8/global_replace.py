def solution(pattern, text, t):
    pre_result = []
    s = pattern + "#" + text
    pi = [0] * len(pattern)
    pi[0] = 0
    pi_prev = 0

    for i in range(1, len(s)):
        k = pi_prev
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1

        if i < len(pattern):
            pi[i] = k

        pi_prev = k

        if k == len(pattern):
            pre_result.append(i - 2 * len(pattern))

    start = 0
    result = ''
    for pos in pre_result:
        result += text[start:pos]
        result += t
        start = pos + len(pattern)

    if start < len(text):
        result += text[start:len(text)]
    return result


def main():
    text = input()
    pattern = input()
    t = input()

    print(solution(pattern, text, t))


if __name__ == '__main__':
    main()
