class Solution(object):
    def limitOccurrences(self, nums, k):
        ans = list()
        count ={}
        for i in nums:
            count[i] = count.get(i,0) + 1
            if(count.get(i,0) <= k):
                ans.append(i)
        
        return ans
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        