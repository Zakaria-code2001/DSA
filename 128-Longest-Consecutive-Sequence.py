class Solution(object):
    def longestConsecutive(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        # 1 lets sort the array
        # if num[i] + 1  = num[i + 1]
        # loop till len nums so we skip the end
        # we can do lenght += 1 every time it's true then we need to store the val in highest length 
        # we can store the in an array or a tuple and get the max at the end
        # using count we cant count and then reset every time the condition is not true and append count to lenghts
        # after storing it we can compare it with current_lenght and keep track of the hihgest and return it

        n = len(nums)
        
        if n == 0:
            return 0

        nums.sort()

        cnt = 1
        maxi = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    cnt += 1
                else:
                    maxi = max(maxi, cnt)
                    cnt = 1

        return max(maxi, cnt)
