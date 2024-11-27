class Solution(object):
    def merge(self, nums1, m, nums2, n):
        \\\
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        \\\
        
        cp_nums = nums1[:m]
        sum_two = sorted(cp_nums + nums2)

        del nums1[:]

        for num in sum_two:
            nums1.append(num)

        