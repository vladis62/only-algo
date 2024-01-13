def calc_prefix_hash(s, q, mod):
    l = len(s) + 1
    hashs = [0] * l
    hashs[1] = ord(s[0])
    for i in range(2, l):
        hashs[i] = (hashs[i - 1] * q + ord(s[i - 1])) % mod
    return hashs


def power_mod(a, exp, mod):
    result = 1
    a %= mod
    while exp > 0:
        if exp & 1 == 1:
            result = (result * a) % mod
        exp >>= 1
        a = (a * a) % mod
    return result


def main():
    a = int(input())
    m = int(input())
    s = input()
    hashs = calc_polinom_hash(s, a, m)
    k = int(input())
    while k > 0:
        l, r = list(map(int, input().split(' ')))
        print((hashs[r] % m - hashs[l - 1] * power_mod(a, r - l + 1, m)) % m)
        k -= 1


if __name__ == '__main__':
    main()
