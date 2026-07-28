class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pred = dummy
        while head:
            if head.next and head.val == head.next.val:
                duplicate_val = head.val
                while head and head.val == duplicate_val:
                    head = head.next
                pred.next = head
            else:
                pred = head
                head = head.next
        return dummy.next
