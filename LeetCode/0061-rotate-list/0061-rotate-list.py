# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        len_, tail = 0, None
        curr_node = head
        while curr_node:
            len_+=1
            tail = curr_node
            curr_node = curr_node.next

        if k%len_ == 0:
            return head
        k %= len_

        curr = head
        for _ in range(len_-k-1):
            curr = curr.next

        newhead = curr.next
        curr.next = None
        tail.next = head

        return newhead
