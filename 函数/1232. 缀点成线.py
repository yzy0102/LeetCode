class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
    # 用斜率做
    #     def checkXY(corr1, corr2, corr3):
    #         if (corr1[0] == corr2[0] or corr2[0] == corr3[0] or corr1[0] == corr3[0]) and not corr1[0]==corr2[0]==corr3[0]:
    #             return 0
    #         if corr1[0]==corr2[0]==corr3[0] or ((corr3[1] - corr2[1]) / (corr3[0] - corr2[0]) == \
    #                 (corr2[1] - corr1[1]) / (corr2[0] - corr1[0])):
    #             return 1
    #         else:
    #             return 0
    #
    #     for i in range(len(coordinates) - 2):
    #         if not checkXY(coordinates[i], coordinates[i+1], coordinates[i+2]):
    #             return False
    #     return True


    # 用向量共线\相关做   全等三角形
        delt_x = coordinates[1][0] - coordinates[0][0]
        delt_y = coordinates[1][1] - coordinates[0][1]
        for i in range(len(coordinates)):
            x = coordinates[i][0] - coordinates[0][0]
            y = coordinates[i][1] - coordinates[0][1]
            if (delt_x * y - delt_y * x):
                return False
        return True

if __name__ == '__main__':
    S = Solution()
    coordinates = [[0,0],[0,1],[0,-1]]
    s = S.checkStraightLine(coordinates)
    print(s)