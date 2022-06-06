# second solution heavily based on https://www.code-recipe.com/post/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # If x is a negative number it is not a palindrome
        # If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
        if x < 0 or (x > 0 and x%10 == 0):   # nice thing to implement from the get go, should've thought about this!
            return False

        reversedNum = 0 # here starts the real comparison, we'll reverse the number to do it
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10 # this makes us not need to tranform the int in str in any step of the solution
            # reversedNum*10 is the process of moving the converted digit to its correct base
            # x%10 was previously the var "lastDigit" 
            x = x // 10 # we are excluding the digits we have already secured in reversedNum (they have already been reversed)

        # If x is equal to reversed number then it is a palindrome
        # If x has odd number of digits, discard the middle digit before comparing with x
        # Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231
        # So, reversedNum/10 = 23, which is equal to x
        return True if (x == reversedNum or x == reversedNum // 10) else False