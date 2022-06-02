class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sumji = 1
        sumhe = 0
        while n:
            index = n %10
            n = n // 10
            sumji = sumji * index
            sumhe = sumhe + index
        return sumji - sumhe


if __name__ == '__main__':
    S = Solution()
    nums = 234
    s = S.subtractProductAndSum(nums)
    print(s)