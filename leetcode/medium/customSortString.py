class Solution(object):
    def customSortString(self, order, s):
        num_order = {}
        pre_s = set(s)
        result = ''

        for i in range(len(order)):
            num_order[order[i]] = [i + 1, 0]

        for i in range(len(s)):
            if s[i] not in num_order:
                num_order[s[i]] = [i * 201, 1]
                continue
            value = num_order.get(s[i])
            num_order[s[i]] = [value[0], value[1] + 1]

        num_order = dict(sorted(num_order.items(), key=lambda x: x[1]))

        for ch, value in num_order.items():
            if ch in pre_s:
                result += ch * value[1]

        return result


def main():
    print(Solution().customSortString("kqep", "pekeq"))


if __name__ == '__main__':
    main()
