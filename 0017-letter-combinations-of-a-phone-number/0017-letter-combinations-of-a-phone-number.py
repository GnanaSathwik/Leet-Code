class Solution(object):
    def letterCombinations(self, digits):
        
        lst = []
        if not digits:
            return lst
        
        map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi' ,
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        

        def fun( index , cur):
            if(index == len(digits)):
                lst.append(cur)
                return
            
            s = digits[index]
            word = (map[s])

            for i in word:
                fun(index+1, cur + i)
        
        fun(0,"")
        return lst


        


        """
        :type digits: str
        :rtype: List[str]
        """
        