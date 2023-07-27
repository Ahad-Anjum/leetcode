class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        values = []
        while (head):
            if head.next not in values:
                values.append(head.next)
            else:
                return True
            head = head.next
        return False