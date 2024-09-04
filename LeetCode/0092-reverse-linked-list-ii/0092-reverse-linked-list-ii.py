# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        N = 1
        node = head
        left_list = []
        rev_list = deque([])
        right_list = []

        if left == right:
            return head

        while node:
            if N < left:
                left_list.append(node.val)
            elif N > right:
                right_list.append(node.val)
            else:
                rev_list.appendleft(node.val)
            node = node.next
            N+=1
            
        return_result = left_list + list(rev_list) + right_list
        new_head = ListNode(return_result[0])
        curr = new_head

        for i in return_result[1:]:
            curr.next = ListNode(i)
            curr = curr.next
                    
        return new_head