class Solution(object):
    def getPermutation(self, n, k):
        lst = [x for x in range(1,n+1)]     
        result = ""   
        while len(lst) != 0 :
            x = factorial(n-1)
            count = (k-1)//x
            result += str(lst[count])
            n -= 1
            k -= count*x
            lst.pop(count)
        
        return result




        """
        :type n: int
        :type k: int
        :rtype: str
        """
        