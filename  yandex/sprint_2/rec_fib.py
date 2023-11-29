def fib(n: int):
    if n == 0 or n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()
