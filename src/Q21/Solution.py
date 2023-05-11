from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = ""
        result += f"{self.val} -> "
        if self.next is not None:
            result += self.next.__str__()
        else:
            result = result.removesuffix(" -> ")
        return result


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        curr = None
        while list1 and list2:
            if list1.val <= list2.val:
                if head is None:
                    head = list1
                    curr = head
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if head is None:
                    head = list2
                    curr = head
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next

        if list1:
            if head is None:
                head = list1
            else:
                curr.next = list1
        if list2:
            if head is None:
                head = list2
            else:
                curr.next = list2
        return head

if __name__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))))
    print(s.mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), None))