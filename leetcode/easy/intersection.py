class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        result = []

        for e in s1:
            if e in s2:
                result.append(e)

        return result


def main():
    print(Solution().intersection([1, 2, 2, 1], [2, 2]))


if __name__ == '__main__':
    main()
