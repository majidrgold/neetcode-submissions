# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        
        current = dummy
        for _ in range(count - n):
            current = current.next
        
        current.next = current.next.next

        return dummy.next

        
