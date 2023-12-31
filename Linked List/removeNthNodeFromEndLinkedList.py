# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head is None or head.next is None:
            return None

        temp = ListNode()
        temp.next = head
        first = temp
        second = temp

        while n > 0:
            second = second.next
            n -= 1

        while second.next != None:
            second = second.next
            first = first.next
        
        first.next = first.next.next

        return temp.next
        