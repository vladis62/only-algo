class Solution(object):
    def majorityElement(self, nums):
        history = {}
        max_num = [-1, 0]

        for num in nums:
            history[num] = history.get(num, 0) + 1
            if max_num[1] < history[num]:
                max_num = [num, history[num]]

        return max_num[0]


def main():
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))


if __name__ == '__main__':
    main()
