class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        """方法一: reduce计数"""
        # dictNum = {}
        # for num in s:
        #     try:
        #         dictNum[num] += 1
        #     except:
        #         dictNum[num] = 1
        #
        # for num in t:
        #     try:
        #         dictNum[num] -= 1
        #         if dictNum[num] < 0:
        #             return num
        #     except:
        #         return num

        """方法二: ASCII码求和"""
        # As = 0
        # at = 0
        # for num in s:
        #     As += ord(num)
        # for num in t:
        #     at += ord(num)
        # return  chr(at - As)

        """方法三: 位运算"""
        # 把s和t拼在一起, 找到出现次数为奇数的数字!!!!!!
        ret = 0
        for num in s:
            ret ^= ord(num)
        for num in t:
            ret ^= ord(num)

        return chr(ret)

if __name__ == '__main__':
    S = Solution()
    s = "abcd"
    t = "abcde"
    s = S.findTheDifference(s, t)
    print(s)