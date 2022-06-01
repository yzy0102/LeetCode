class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x - 1

        if x == 1 or x== 2:
            return 1
        while left < right:
            mid = ((right - left) >> 1) + left
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return left - 1


if __name__ == '__main__':
    S = Solution()
    x = 3
    s = S.mySqrt(x)
    print(s)