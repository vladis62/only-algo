def equals_def(str1, str2):
    dictionary = {}

    new_str1 = new_str2 = ''

    for i in range(26):
        dictionary[chr(ord('a') + i)] = (i + 1) % 2

    for c in str1:
        if dictionary[c] == 0:
            new_str1 += c

    for c in str2:
        if dictionary[c] == 0:
            new_str2 += c

    if new_str1 > new_str2:
        return 1
    elif new_str1 == new_str2:
        return 0
    else:
        return -1


def main():
    str1 = input()
    str2 = input()
    print(equals_def(str1, str2))


if __name__ == '__main__':
    main()
