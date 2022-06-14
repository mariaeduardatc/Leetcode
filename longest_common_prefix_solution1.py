class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs_len = len(strs)
        prefix = ""
        strs_min = len(min(strs, key=len))
        
        
        for j in range(strs_min): # so we don't compare letters with ones 
            # that do not exist in other words
            
            for i in range(strs_len): # comparisons
                if strs[0][j] != strs[i][j]:
                    return prefix
                      
            prefix += strs[0][j]  # addition   
        
        return prefix