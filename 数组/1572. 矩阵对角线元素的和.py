class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        n = len(mat)
        Sum = 0
        if n == 1:
            return mat[0][0]

        for i in range(n):
            Sum += mat[i][i] + mat[i][n-i-1]
        if n&1:#判断为奇数
            return Sum - mat[n//2][n//2]
        else:
            return Sum


if __name__ == '__main__':
    S = Solution()
    mat = [[7,9,8,6,3],
           [3,9,4,5,2],
           [8,1,10,4,10],
           [9,5,10,9,6],
           [7,2,4,10,8]]
    s = S.diagonalSum(mat)
    print(s)