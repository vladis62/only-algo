import math


def solution(n):
    i = n
    k = 2
    arr = list()
    sqrt_n = int(math.sqrt(n)) + 1
    while k <= sqrt_n:
        if k * k > i and n == i:
            break
        if n % k == 0:
            arr.append(k)
            n //= k
        else:
            k += 1
    if n > 1:
        arr.append(n)
    if not arr:
        return str(i)
    return ' '.join(list(map(str, arr)))


def main():
    n = int(input())
    result = solution(n)
    print(result)


if __name__ == '__main__':
    main()
