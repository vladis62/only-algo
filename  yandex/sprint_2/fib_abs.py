def fib(n: int, k: int):
    fibs = [1, 1]
    i = 2
    p = pow(10, k)
    while i <= n:
        fibs.append((fibs[i - 2] + fibs[i - 1]) % p)
        i += 1
    return fibs[n]


def main():
    n, k = list(map(int, input().split()))
    print(fib(n, k))


if __name__ == '__main__':
    main()
