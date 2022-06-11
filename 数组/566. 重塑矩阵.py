class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # n = len(mat)
        # m = len(mat[0])
        # if r*c != n*m:
        #     return mat
        # result = []
        # for i in range(n):
        #     for j in range(m):
        #         result.append(mat[i][j])
        #
        # result_mat = []
        # print(result)
        # k = 0
        # for i in range(r):
        #     temp = []
        #     for j in range(c):
        #         temp.append(result[k])
        #         k += 1
        #     result_mat.append(temp)
        # return result_mat

        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = mat[x // n][x % n]
        return ans
if __name__ == '__main__':
    S = Solution()
    mat = [[1, 2], [3, 4]]
    r = 2
    c = 2

    s = S.matrixReshape(mat, r, c)
    print(s)