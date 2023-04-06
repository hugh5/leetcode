from typing import Optional


class Solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        curr = head
        next = head.next

        while next is not None:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        curr.next = prev
        return curr