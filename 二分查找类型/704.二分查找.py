class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        right = n - 1
        left = 0



        while left < right:
            mid = ((right - left) >> 1) + left

            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        if nums[left] == target:
            return left
        else:
            return -1


if __name__ == '__main__':
    S = Solution()
    nums = [1, 3, 5, 6]
    target = -1
    s = S.search(nums, target)
    print(s)