class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Base case: if list is empty or has only one node, it is already sorted
        if not head or not head.next:
            return head
            
        # 1. Split the list into two halves
        left = head
        right = self.get_mid(head)
        
        # 2. Recursively sort both halves
        left = self.insertionSortList(left)
        right = self.insertionSortList(right)
        
        # 3. Merge the two sorted halves back together
        return self.merge(left, right)
        
    def get_mid(self, head: ListNode) -> ListNode:
        # Uses slow and fast pointers to find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Disconnect the left half from the right half
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Merges two sorted linked lists using a dummy node
        dummy = ListNode(0)
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Append any remaining nodes from either list
        tail.next = list1 if list1 else list2
        return dummy.next
