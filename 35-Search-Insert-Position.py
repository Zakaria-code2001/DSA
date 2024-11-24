class Solution(object):
    def searchInsert(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: int
        \\\
        for num in nums:
            if num > target:
                return nums.index(num)
            elif num == target:
                return nums.index(num)
            
        return len(nums)
        