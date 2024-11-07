class Solution(object):
    def twoSum(self, nums, target):
        \\\
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        \\\
        num_to_index = {}
        for index, value in enumerate(nums):
            num_to_index[value] = index
        for index, value in enumerate(nums):
            complement = target - value
            if complement in num_to_index and num_to_index[complement] != index:
                return [index, num_to_index[complement]]
        return []


