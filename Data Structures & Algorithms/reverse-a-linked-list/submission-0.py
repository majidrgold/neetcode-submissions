# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # 1. Recursion
        # if not head:
        #     return None
        
        # new_head = head
        # if head.next:
        #     new_head = self.reverseList(head.next)
        #     head.next.next = head
        
        # head.next = None

        # return new_head
        # # t: O(n), s: O(n)
        # ---
        # 2. Iterative
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        return prev


        