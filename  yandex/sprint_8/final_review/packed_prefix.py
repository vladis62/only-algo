# ID - 110298615
# -- ПРИНЦИП РАБОТЫ --
# декодируем строку, ищем наибольший префикс двух строк
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
#  O(n * k), n - количество строк, k - самая длинная распакованная строкиа
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
#  O(k), k - самая длинная строка

def decode_string(string):
    result = ''
    num = 0
    stack = []

    for ch in string:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append(num)
            stack.append(result)
            result = ''
            num = 0
        elif ch == ']':
            pre_result = stack.pop()
            num = stack.pop()
            result = pre_result + result * num
            num = 0
        else:
            result += ch
    return result


def max_prefix(prefix, strings):
    prefix_len = len(prefix)
    for string in strings:
        while string[:prefix_len] != prefix and prefix_len:
            prefix_len -= 1
            prefix = prefix[:prefix_len]

    return prefix


def main():
    n = int(input())

    if n == 0:
        print('')

    prefix = decode_string(input())
    strings = []
    for _ in range(n-1):
        strings.append(decode_string(input()))

    print(max_prefix(prefix, strings))


if __name__ == '__main__':
    main()
