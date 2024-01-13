def calc_prefix_hash(s, a, mod):
    l = len(s)
    result = 0
    for i in range(0, l):
        if i != l - 1:
            result = (result + ord(s[i])) * a
        else:
            result += ord(s[i])
        result %= mod
    return result % mod


def main():
    a = int(input())
    m = int(input())
    s = input()
    print(calc_prefix_hash(s, a, m))


if __name__ == '__main__':
    main()

# 1-5
# bc
# 2-3
# a

