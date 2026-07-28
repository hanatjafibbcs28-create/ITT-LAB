class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            node_id = id(head)
            if node_id in seen:
                return head
            seen.add(node_id)
            head = head.next
        return None
