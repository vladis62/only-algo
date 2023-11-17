def solution(words, n):
    max_word = ''
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word


def main():
    n = int(input())
    arr = list(map(str, input().split()))
    result = solution(arr, n)
    print(result)
    print(len(result))


if __name__ == '__main__':
    main()
