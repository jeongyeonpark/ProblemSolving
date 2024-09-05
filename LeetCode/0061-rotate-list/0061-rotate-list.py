# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head

        nodes = []
        curr_node = head
        while curr_node:
            nodes.append(curr_node.val)
            curr_node = curr_node.next

        if k%len(nodes)==0:
            return head

        n = k%len(nodes)
        new_node = nodes[-n:]+nodes[:-n]
        head2 = ListNode(new_node[0])
        curr_node = head2
        for i in new_node[1:]:
            curr_node.next = ListNode(i)
            curr_node = curr_node.next
        return head2
