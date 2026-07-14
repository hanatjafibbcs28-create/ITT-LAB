# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: If list is empty or has 1 node, no sorting needed
        if not head or not head.next:
            return head
        
        # 1. Collect all node values into a standard Python list
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
            
        # 2. Sort the values using Python's blazing fast, C-optimized Timsort
        values.sort()
        
        # 3. Overwrite the values back into the original linked list structure
        current = head
        for val in values:
            current.val = val
            current = current.next
            
        return head
