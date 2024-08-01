# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        prev_list = []
        next_list = []
        list_ = []

        curr_node = head
        while curr_node:
            list_.append(curr_node.val)
            if curr_node.val < x:
                prev_list.append(curr_node.val)
            else:
                next_list.append(curr_node.val)
            curr_node = curr_node.next

        if list_ == prev_list+next_list:
            return head
        curr_node = head
        for n in prev_list+next_list:
            curr_node.val = n
            curr_node = curr_node.next

        return head
