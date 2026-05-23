'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        num = nums1 + nums2
        num.sort()
        n = len(num)
        if(n%2 == 1):
            return num[n//2]
        return (num[n//2 -1] + num[n//2]) / 2.0
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        