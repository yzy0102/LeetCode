class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # ---顺序查找---
        # last = 0
        # while last != len(nums):
        #     if nums[last] < target:
        #         last += 1
        #     else:
        #         return last
        #
        # if target <= nums[0]:
        #     return 0
        # return len(nums)

        # ---二分查找---
        n = len(nums)
        left = 0
        right = n

        while left < right:
            mid = ((right - left) >> 1) + left
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left




if __name__ == '__main__':
    S = Solution()
    nums = [1, 3, 5, 6]
    target = 7
    s = S.searchInsert(nums, target)
    print(s)