import sys


def solution(a, b, c):
    if a % 2 == 1 and b % 2 == 1 and c % 2 == 1:
        return 'WIN'
    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        return 'WIN'
    return 'FAIL'


def main():
    line = sys.stdin.readline().rstrip()
    a, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    result = solution(a, b, c)
    print(result)


if __name__ == '__main__':
    main()
