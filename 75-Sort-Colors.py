class Solution(object):
    def sortColors(self, nums):
        \\\
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        \\\
        red = 0
        white = 1
        blue = 2
        red_arr = []
        white_arr = []
        blue_arr = []

        for num in nums:
            if num == red:
                red_arr.append(num)
            elif num == white:
                white_arr.append(num)
            elif num == blue:
                blue_arr.append(num)

        i = 0
        for num in red_arr + white_arr + blue_arr:
            nums[i] = num
            i += 1