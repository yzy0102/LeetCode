class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """

        max_distance = 10**5
        min_index = -1
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                manhattan_distance = abs(x - point[0]) + abs(y - point[1])
                if manhattan_distance < max_distance:
                    max_distance = manhattan_distance
                    min_index = index
        return min_index


if __name__ == '__main__':
    S = Solution()
    x = 3
    y = 4
    points = [[1,2]]
    s = S.nearestValidPoint(x, y, points)
    print(s)