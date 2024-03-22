def count_change(s1, s2):
    s1, s2 = [s1, s2] if len(s1) >= len(s2) else [s2, s1]
    if len(s1) - len(s2) > 1:
        return "FAIL"

    if len(s1) <= 1 and len(s2) <= 1 or (s1 == s2):
        return "OK"

    if len(s1) == len(s2):
        count_wrong = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count_wrong += 1
                if count_wrong > 1:
                    return "FAIL"
    else:
        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1

        while i < len(s2):
            if s1[i + 1] != s2[i]:
                return "FAIL"
            i += 1
    return "OK"


def main():
    str1 = input()
    str2 = input()
    print(count_change(str1, str2))


if __name__ == '__main__':
    main()

# abcdehg
# abdefg
