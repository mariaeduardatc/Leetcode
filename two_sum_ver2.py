class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # trying a new solution using a hashmap (studying a new method)
        
        numMap = {} # val : index
        
        for i, n in enumerate(nums): # i is the index and n the value
            diff = target - n # the difference is the number we need to find so diff + n equals the target
            if diff in numMap:
                return [numMap[diff], i] # getting indexes
            numMap[n] = i