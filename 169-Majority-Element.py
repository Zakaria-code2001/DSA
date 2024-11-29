class Solution(object):
    def majorityElement(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\

        unique_nums = set(nums)

        dict_nums = {}

        for num in unique_nums:
            dict_nums[num] = nums.count(num)

        greatest_key = max(dict_nums, key=dict_nums.get)

        return greatest_key