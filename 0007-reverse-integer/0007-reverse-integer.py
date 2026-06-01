class Solution(object):
    def reverse(self, x):
        x = list(str(x))
        if(x[0] == '-'):
            x =list(x[0])+x[:0:-1]
        else:
            x = x[::-1]
        r = int(''.join(x))
        if r<-2**31 or r>2**31 -1:
            return 0
        return r
        """
        :type x: int
        :rtype: int
        """
        