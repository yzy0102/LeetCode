class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = 0
        # while n != 0:
        #     if n % 2 == 0:
        #         n = n >> 1
        #     else:
        #         count += 1
        #         n = n >> 1
        # return count

        #优化思路 让n与n-1做&运算
        ret = 0
        while n:
            n &= n - 1
            ret += 1
        return ret

if __name__ == '__main__':
    S = Solution()
    nums = 0b00000000000101011
    s = S.hammingWeight(nums)
    print(s)
    print(8 & 7)