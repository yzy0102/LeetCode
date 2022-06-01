class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        """
        #超时的垃圾
        count = 0
        for num in range (low, high+1):
            if num % 2 == 1:
                count += 1
        return count
        """
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    S = Solution()
    s = S.countOdds(3, 7)
    print(s)
