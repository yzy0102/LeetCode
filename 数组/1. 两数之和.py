class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        法1: 双指针 O(n^2)
        """
        # left = 0
        # right = 1
        # n = len(nums)
        # while True:
        #     if (nums[right] + nums[left]) == target:
        #         return [left, right]
        #     else:
        #         right += 1
        #
        #     if right == n:
        #         left += 1
        #         right = left + 1

        """
        法2: hash表
        """
        hash_dict = {}
        for i, num in enumerate(nums):
            if target - num in hash_dict:
                return [hash_dict[target-num], i]
            hash_dict[num] = i
        return []



if __name__ == '__main__':
    S = Solution()
    nums =[3, 1, 2, 3]
    target = 6
    s = S.twoSum(nums, target)
    print(s)