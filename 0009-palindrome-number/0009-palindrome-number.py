class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        lst= []
        num = x
        while num != 0:
            lst.append(num % 10)
            num = num // 10
        
        
        for i in lst:
            num = num *10 + i
        
        return num == x

        """
        :type x: int
        :rtype: bool
        """
        