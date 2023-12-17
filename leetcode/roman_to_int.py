symbol_value = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_int(self, s):
    value = 0
    for i in range(len(s) - 1):
        if symbol_value[s[i]] < symbol_value[s[i + 1]]:
            value -= symbol_value[s[i]]
        else:
            value += symbol_value[s[i]]
    return value + symbol_value[s[-1]]


if __name__ == '__main__':
    print(roman_to_int('PyCharm', 'MCMXCIV'))
