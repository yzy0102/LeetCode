class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        different_count = 0
        index = list()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                index.append(i)
                different_count += 1
            if different_count > 2:
                return False

        if different_count == 0:
            return True
        if different_count == 1:
            return False

        if different_count == 2 and s1[index[0]] == s2[index[1]] and s1[index[1]] == s2[index[0]]:
            return True
        else:
            return False




if __name__ == '__main__':
    S = Solution()
    s1 = "npv"
    s2 = "zpn"

    s = S.areAlmostEqual(s1, s2)
    print(s)