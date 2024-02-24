# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        history = {}
        for e in arr:
            history[e] = history.get(e, 0) + 1
        if k == 0:
            return len(history)
        history = dict(sorted(history.items(), key=lambda x: x[1]))
        count = 0
        for key, v in history.items():
            while history[key] > 0:
                history[key] -= 1
                k -= 1
                if k == 0:
                    for key_i, v_i in history.items():
                        if v_i > 0:
                            count += 1
                    return count
        return count


def main():
    print(Solution().findLeastNumOfUniqueInts([2, 4, 1, 8, 3, 5, 1, 3], 3))


if __name__ == '__main__':
    main()
