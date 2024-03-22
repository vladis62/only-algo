class Solution(object):
    def maxFrequencyElements(self, nums):
        history = [0] * 100

        for num in nums:
            history[num] += 1

        max_count = max(history)
        max_elems = []
        for i in range(len(history)):
            if history[i] == max_count:
                max_elems.append(i)

        return len(list(filter(lambda num: num in max_elems, nums)))


def main():
    print(Solution().maxFrequencyElements([1, 2, 2, 3, 1, 4]))


if __name__ == '__main__':
    main()
