class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # O(nnn) 70%
        # n = len(arr)
        # p_head = 0
        # Sum = 0
        # times = (n - 1) // 2 + 1
        # for time in range(0, times):
        #     p_end = 2 * time
        #     for i in range(0, n - p_end):
        #         Sum += sum(arr[p_head+i: p_end+i+1])
        # return Sum

        #O(nnn) -> O(n)  数学方法, 左右两边的字数均为奇数或为偶数
        sum = 0
        n = len(arr)
        for i, v in enumerate(arr):
            leftCount, rightCount = i, n - i - 1
            leftOdd = (leftCount + 1) // 2
            rightOdd = (rightCount + 1) // 2
            leftEven = leftCount // 2 + 1
            rightEven = rightCount // 2 + 1
            sum += v * (leftOdd * rightOdd + leftEven * rightEven)
        return sum


if __name__ == '__main__':
    S = Solution()
    arr = [10,11,12]
    s = S.sumOddLengthSubarrays(arr)
    print(s)