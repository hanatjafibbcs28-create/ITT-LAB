from typing import Optional
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        isVisited = set()
        tempA = headA
        while tempA:
            isVisited.add(tempA)
            tempA = tempA.next
        tempB = headB
        while tempB:
            if tempB in isVisited:
                return tempB
            tempB = tempB.next
        return None
