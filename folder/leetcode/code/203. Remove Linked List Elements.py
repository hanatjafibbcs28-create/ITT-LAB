# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node that points to head
        dummy = ListNode(0)
        dummy.next = head
        
        current = dummy
        
        # Traverse the list using the next pointer
        while current.next:
            if current.next.val == val:
                # Bypass the matching node
                current.next = current.next.next
            else:
                # Move to the next node only if we didn't perform a deletion
                current = current.next
                
        return dummy.next
