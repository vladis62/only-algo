def strange_equals(str1, str2):
    dictionary1 = {}
    dictionary2 = {}
    if len(str1) != len(str2):
        return 'NO'
    for i in range(len(str1)):
        if str1[i] in dictionary1:
            ch = dictionary1[str1[i]]
            if ch != str2[i]:
                return 'NO'
        else:
            dictionary1[str1[i]] = str2[i]
        dictionary2[str2[i]] = str1[i]
    return 'YES' if len(dictionary1) == len(dictionary2) else 'NO'


def main():
    str1 = input()
    str2 = input()
    print(strange_equals(str1, str2))


if __name__ == '__main__':
    main()
