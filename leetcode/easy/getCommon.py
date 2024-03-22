class Solution(object):
    def getCommon(self, nums1, nums2):
        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                return nums2[i2]

        return -1


def main():
    print(Solution().getCommon([1, 1, 2], [2, 4]))


if __name__ == '__main__':
    main()
