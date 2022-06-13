class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """ 算法二:排序  O(NlogN) """
        """ 算法一: 创建hashmap计数 时间复杂度O(n)"""
        num_hashmap = {}
        for num in nums:
            try:
                num_hashmap[num] += 1
            except:
                num_hashmap[num] = 1
            if num_hashmap[num] >= 2:
                return True
        return False








if __name__ == '__main__':
    S = Solution()
    nums = [1,2,3,1]
    s = S.containsDuplicate(nums)
    print(s)