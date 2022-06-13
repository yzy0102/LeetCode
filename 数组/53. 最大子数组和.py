class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """算法一: 遍历 O(N^2) 太垃圾了超时了"""
        # max_result = - 100000
        # if len(nums) == 1:
        #     return nums[0]
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         Sum = sum(nums[i:j+1])
        #         if Sum > max_result:
        #             max_result = Sum
        #
        # return max_result

        # """s算法二: 先找到最大值的位置, 从最大值位置向两边搜索 错误思路, 因为有多个最大值位置, rnm 退钱"""
        # max_index = nums.index(sorted(nums)[-2])
        # max_result = - 100000
        # # 分别定义左指针和右指针
        # right = max_index
        # left = max_index
        # while right <= len(nums):
        #     right += 1
        #     while left >= 0:
        #         temp = sum(nums[left:right])
        #         if temp > max_result:
        #             max_result = temp
        #         left -= 1
        #     left = max_index![]
        # return max(max_result, nums[max_index])

        """算法二:  贪心算法"""
        # pre = 0
        # maxAns = nums[0]
        # for x in nums:
        #     pre = max(pre + x, x)
        #     maxAns = max(maxAns, pre)
        # return maxAns
        """动态规划 O(n)"""
        n = len(nums)
        for i in range(1, n):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
        return max(nums)

        """算法四: 分治"""


if __name__ == '__main__':
    S = Solution()
    nums = [-3,-2,-3,-3,-1,-3,0]
    s = S.maxSubArray(nums)
    print(s)