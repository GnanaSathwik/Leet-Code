class Solution(object):
    def getPermutation(self, n, k):
        lst = [x for x in range(1,n+1)]
        fact = [1] * 10
        for i in range(1, 10):
            fact[i] = fact[i - 1] * i
            
        result = ""   
        while len(lst) != 0 :
            count = 0
            x = fact[n-1]
            num = x
            while k > num :
                count += 1
                num += x
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
        