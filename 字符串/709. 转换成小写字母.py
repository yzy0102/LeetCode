class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_num = ""
        for num in s:
            if ord(num) <= 90 and ord(num) >= 65:   #65-90 A-Z  97-122
                new_num += chr(ord(num) + 32)
            else:
                new_num += num
        return new_num

if __name__ == '__main__':
    S = Solution()
    s = "Hello"
    s = S.toLowerCase(s)
    print(s)