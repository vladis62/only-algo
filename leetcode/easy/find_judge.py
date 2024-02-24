class Solution(object):
    def findJudge(self, n, trust):
        history_in = [0] * (n + 1)
        history_out = [0] * (n + 1)
        for t in trust:
            history_in[t[0]] += 1
            history_out[t[1]] += 1

        for i in range(1, n + 1):
            if (history_out[i] == n - 1) and history_in[i] == 0:
                return i

        return -1


def main():
    print(Solution().findJudge(3, [[1, 3], [2, 3]]))


if __name__ == '__main__':
    main()
