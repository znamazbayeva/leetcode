# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None:
            return None
        if list1 is None or list2 is None:
            return list1 or list2
        node = ListNode()
        def helper(node, l1, l2):
            if l1 is None and l2 is None:
                return None
            if l1 is None or l2 is None:
                node.val = l1.val if l1 else l2.val
                node.next = l1 and l1.next or l2 and l2.next
            else:
                if l1.val <= l2.val:
                    node.val = l1.val
                    node.next = helper(ListNode(), l1.next, l2)
                else:
                    node.val = l2.val
                    node.next = helper(ListNode(), l1, l2.next)
            return node      
        return helper(node, list1, list2)
            
        