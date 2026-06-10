class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        if x % 10 == 0 and x != 0:
            return False

        
        num = x
        rev = 0
        while num > rev:
            rev = rev * 10 + (num % 10)
            num = num // 10

        
        return num == rev or  num == rev //10 
        
        
        """
        :type x: int
        :rtype: bool
        """
        