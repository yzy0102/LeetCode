class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        equal = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != equal:
                return False
        return True


if __name__ == '__main__':
    S = Solution()
    arr = [3,5,1]
    s = S.canMakeArithmeticProgression(arr)
    print(s)
