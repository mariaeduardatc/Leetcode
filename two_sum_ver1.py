class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # compare sums to the target value
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        indices = [i, j]
                        return indices