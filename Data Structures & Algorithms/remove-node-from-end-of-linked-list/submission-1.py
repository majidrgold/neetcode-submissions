# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # # 1. Two Pass
        # dummy = ListNode(0, head)
        # count = 0
        # node = head
        # while node:
        #     count += 1
        #     node = node.next
        
        # current = dummy
        # for _ in range(count - n):
        #     current = current.next
        
        # current.next = current.next.next

        # return dummy.next
        # # T: O(n), M: O(1)
        # --- 
        # 2. One Pass
        dummy = ListNode(0, head)
        left, right = dummy, head
        for _ in range(n):
            right = right.next
        
        while left and right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next




        
