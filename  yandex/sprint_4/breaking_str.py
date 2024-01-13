import itertools


def breaking():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hash_to_word = {}
    for length in range(1, 6):
        for combination in itertools.product(alphabet, repeat=length):
            string = ''.join(combination)
            hash = calc_polinom_hash(string, 1000, 123987123)
            if hash in hash_to_word:
                return hash_to_word[hash], string
            else:
                hash_to_word[hash] = string


def calc_polinom_hash(s, a, mod):
    k = 3
    l = len(s)
    result = 0
    for i in range(0, l):
        if i % k == 0 and i != l:
            result %= mod
        if i != l - 1:
            result = (result + ord(s[i])) * a
        else:
            result += ord(s[i])
    return result % mod


def main():
    print(breaking())


if __name__ == '__main__':
    main()
