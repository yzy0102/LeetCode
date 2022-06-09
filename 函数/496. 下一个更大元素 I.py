class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # result = []
        # def find_next_max_number(number):
        #     for i in range(nums2.index(number), len(nums2)):
        #         if nums2[i] > number:
        #             return nums2[i]
        #     return -1
        #
        # for i in range(len(nums1)):
        #     number = nums1[i]
        #     result.append(find_next_max_number(number))
        # return result

        # 单调栈 + 哈希表
        res = {}
        stack = []
        # 用单调栈stack存储紧跟num的更大数字
        for num in reversed(nums2):
            while stack and num >= stack[-1]:
                stack.pop()
            res[num] = stack[-1] if stack else -1
            stack.append(num)


        print(stack)
        print(res)

        return [res[num] for num in nums1]

if __name__ == '__main__':
    S = Solution()
    nums1 = [2, 4]
    nums2 = [2,5,3,6,8,4,7,1]
    s = S.nextGreaterElement(nums1, nums2)
    print(s)
