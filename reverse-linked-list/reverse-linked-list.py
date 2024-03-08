# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    d = None
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        1,2,3,4,5
        1->2->3->4->5
        1->2->1 3->4->5
        """
        def helper(h, prev=None):
            if not h:
                return prev
            n = h.next
            h.next = prev
            return helper(n, h)
        return helper(head)
        
        