class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i = len(nums) - 1
        while True:
            if ((nums[i] - nums[i-2] < nums[i-1]) and (nums[i-1] + nums[i-2] > nums[i])):
                return nums[i] + nums[i-1] + nums[i-2]
            else:
                i-=1
            if i == 1:
                return 0



if __name__ == '__main__':
    S = Solution()
    nums = [1,2,1]
    s = S.largestPerimeter(nums)
    print(s)