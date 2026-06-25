class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        cur_sum = 0
        head = head.next

        while head:
            if head.val == 0:
                tail.next = ListNode(cur_sum)
                tail = tail.next
                cur_sum = 0
            else:
                cur_sum += head.val

            head = head.next

        return dummy.next
