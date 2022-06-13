class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)

        new_word = ""
        if n > m:
            for i in range(m):
                new_word += word1[i]
                new_word += word2[i]
            new_word += word1[m:]
        else:
            for i in range(n):
                new_word += word1[i]
                new_word += word2[i]
            new_word += word2[n:]
        return new_word
if __name__ == '__main__':
    S = Solution()
    word1 = "abcd"
    word2 = "pq"

    s = S.mergeAlternately(word1, word2)
    print(s)