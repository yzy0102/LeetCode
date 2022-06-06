class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 1
        for num in nums:
            product *= num
        if product > 0:
            return 1
        elif product == 0:
            return 0
        else:
            return -1


if __name__ == '__main__':
    S = Solution()
    nums = [-1,-2,-3,-4,3,2,1]
    s = S.arraySign(nums)
    print(s)