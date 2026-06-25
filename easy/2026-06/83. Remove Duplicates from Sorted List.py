# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
 class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            t = curr.next
            if t.val == curr.val:
                curr.next = t.next
                continue
            curr = t
        return curr
