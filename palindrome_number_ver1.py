import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def countDigits(n): # acho que nao preciso disso?
            if n > 0:
                digits = int(math.log10(n))+1
            elif n == 0:
                digits = 1
            else:
                digits = int(math.log10(-n))+2 # +1 if you don't count the '-' 
            return digits
        
        def Convert(string):
            list1=[]
            list1[:0]=string
            return list1
        
        numMap = {} # hashMap index : digit
        digits = countDigits(x)
        list_test = str(x)
        listDigits = Convert(list_test)
        
        print(listDigits, list_test)
        
        for i, n in enumerate(listDigits):  # i is the index and n the digit
            numMap[i] = n # saving everything on the hashmap
        for j in range(digits): # i need to compare stuff now
            if numMap[j] != numMap[digits-(j+1)]:
                return False
        return True