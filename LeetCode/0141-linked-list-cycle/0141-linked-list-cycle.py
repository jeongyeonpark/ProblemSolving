# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if not head:
        #     return False

        # node = head
        # next_node = head.next
        # visited_node = []
        # while not next_node:
        #     node_id = id(node)
        #     if not node_id in visited_node:
        #         visited_node.append(node_id)
        #         node = next_node
        #         next_node = next_node.next

        #     else:
        #         return True
        # return False
        if not head:
            return False

        node = head

        visited_node =[]
        
        while node.next:
            id_node = id(node)
            if id_node in visited_node:
                return True
            visited_node.append(id_node)
            node = node.next

        return False