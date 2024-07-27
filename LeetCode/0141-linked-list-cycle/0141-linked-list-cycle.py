# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        node = head
        next_node = head.next
        visited_node = []
        while node != None:
            node_id = id(node)
            if not next_node:
                return False

            elif not node_id in visited_node:
                visited_node.append(node_id)
                node = next_node
                next_node = next_node.next

            else:
                return True
