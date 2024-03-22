def reverse_str(strings):
    left = 0
    right = len(strings) - 1

    while left < right:
        strings[left], strings[right] = strings[right], strings[left]
        left += 1
        right -= 1

    return strings


def main():
    strings = list(map(str, input().split()))
    print(*reverse_str(strings))


if __name__ == '__main__':
    main()
