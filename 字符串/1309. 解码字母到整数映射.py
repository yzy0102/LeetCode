class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 97-122 : a-z
        left = 0
        right = 2
        n = len(s)
        new = ""
        while left < n:
            try:
                if s[right]=="#":
                    num = int(s[left:right]) + 96
                    new += chr(num)
                    left += 3
                    right += 3
                else:
                    new += chr(int(s[left]) + 96)
                    right+=1
                    left+=1
            except:
                new += chr(int(s[left]) + 96)
                right += 1
                left += 1
        return new


if __name__ == '__main__':
    S = Solution()
    s = "10#11#12"
    s = S.freqAlphabets(s)
    print(s)
