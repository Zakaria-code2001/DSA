class Solution(object):
    def pivotIndex(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        for i in range(len(nums)):
            left_sum = sum(tuple(nums[:i]))
            rigth_sum = sum(tuple(nums[:i:-1]))

            pivot_index = -1
            if left_sum == rigth_sum:
                pivot_index = i
                return pivot_index
        return pivot_index
        