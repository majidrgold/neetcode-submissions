# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Recursion
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        


        # ---
        # # 2. Iterative
        # dummy = ListNode()
        # tail = dummy
        
        # l1, l2 = list1, list2

        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next
        #     tail = tail.next
        
        # tail.next = l1 if l1 else l2

        # return dummy.next
        # T: O(n), M: O(n)

        