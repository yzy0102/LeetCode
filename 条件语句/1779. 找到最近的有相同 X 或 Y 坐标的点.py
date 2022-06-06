class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """




if __name__ == '__main__':
    S = Solution()
    x = 3
    y = 4
    points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    s = S.nearestValidPoint(x, y, points)
    print(s)