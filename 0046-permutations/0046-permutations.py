class Solution(object):
    def permute(self, nums):
        result =[]
        n = len(nums)
        def swap_recursion(index):
            if(index == len(nums)):
                result.append(nums[:])
            for i in range(index,len(nums)):
                nums[index] , nums[i] = nums[i] , nums[index]
                swap_recursion(index+1)
                nums[index] , nums[i] = nums[i],nums[index]
        swap_recursion(0)
        return result

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        