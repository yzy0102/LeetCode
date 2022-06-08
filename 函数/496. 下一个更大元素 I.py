class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        def find_next_max_number(number):
            for i in range(nums2.index(number), len(nums2)):
                if nums2[i] > number:
                    return nums2[i]
            return -1

        for i in range(len(nums1)):
            number = nums1[i]
            result.append(find_next_max_number(number))
        return result


if __name__ == '__main__':
    S = Solution()
    nums1 = [2, 4]
    nums2 = [1,2,3,4]
    s = S.nextGreaterElement(nums1, nums2)
    print(s)
