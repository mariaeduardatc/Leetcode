class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenght = len(nums)
        list_ordered = nums.sort()
        
        for i in range(lenght):
            if nums[i] != i:
                return i
        return i+1