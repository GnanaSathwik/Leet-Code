'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):

        temp = ListNode(0)
        temp.next = head
         
        p = temp
        while p.next and p.next.next:
            a = p.next
            b = p.next.next

            a.next = b.next
            b.next = a
            p.next = b

            p = a
        return temp.next

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        