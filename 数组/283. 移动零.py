class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """解法1: O(4n) 暴力解法"""
        # for index, num in enumerate(nums):
        #     if num == 0:
        #         nums.append(0)
        #         nums.pop(index)
        # for index, num in enumerate(nums):
        #     if num == 0:
        #         nums.append(0)
        #         nums.pop(index)
        # for index, num in enumerate(nums):
        #     if num == 0:
        #         nums.append(0)
        #         nums.pop(index)
        # for index, num in enumerate(nums):
        #     if num == 0:
        #         nums.append(0)
        #         nums.pop(index)


        """解法2: O(n) 很慢"""
        # i = 0
        # n = len(nums)
        # while i < n:
        #     if nums[i] == 0:
        #         nums.pop(i)
        #         nums.append(0)
        #         n -= 1
        #     else:
        #         i += 1
        # return nums


        """解法3: 替换? 其实和解法2是一样的 """
        # i = 0
        # n = len(nums)
        # while i < n:
        #     if nums[i] == 0:
        #         nums[i:] = nums[i+1:]
        #         nums.append(0)
        #         n -= 1
        #     else:
        #         i += 1
        # return nums
        """解法4 双指针"""
        left = 0
        right = 0
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

if __name__ == '__main__':
    S = Solution()
    nums = [0,0,1,0,3,12]
    s = S.moveZeroes(nums)
    print(s)