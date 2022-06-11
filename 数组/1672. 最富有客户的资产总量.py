class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max([sum(acc) for acc in accounts])

if __name__ == '__main__':
    S = Solution()
    accounts = [[1,2,3],[3,2,1]]
    s = S.maximumWealth(accounts)
    print(s)