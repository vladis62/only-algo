def bracers_generator(left, right, prefix):
    if left == 0 and right == 0:
        print(prefix)
    else:
        if left > 0:
            bracers_generator(left - 1, right, prefix + '(')
        if left < right:
            bracers_generator(left, right - 1, prefix + ')')


def main():
    n = int(input())
    bracers_generator(n, n, '')


if __name__ == '__main__':
    main()
