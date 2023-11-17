import string


def solution(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] in string.punctuation or s[left] == ' ' or s[left] in range(0, 9):
            left += 1
            continue
        if s[right] in string.punctuation or s[right] == ' ' or s[left] in range(0, 9):
            right -= 1
            continue
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    s = input().lower()
    result = solution(s)
    print(result)


if __name__ == '__main__':
    main()
