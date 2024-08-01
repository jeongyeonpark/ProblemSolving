# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # prev_list = []
        # next_list = []

        # curr_node = head
        # while curr_node:
        #     if curr_node.val < x:
        #         prev_list.append(curr_node.val)
        #     else:
        #         next_list.append(curr_node.val)
        #     curr_node = curr_node.next

        # curr_node = head
        # for n in prev_list+next_list:
        #     curr_node.val = n
        #     curr_node = curr_node.next

        # return head

        prev_node = ''
        curr_node = head

        while curr_node != None:
            if curr_node.val >= x:
                head_node = curr_node
                while curr_node.next != None and curr_node.next.val >= x:
                    curr_node = curr_node.next

                if not curr_node.next:
                    return head
                    
                next_node = curr_node.next
                start_node = curr_node.next
                end_node = curr_node.next

                while next_node != None and next_node.val < x:
                    end_node = next_node
                    next_node = end_node.next

                curr_node.next = end_node.next

                if prev_node == '':
                    end_node.next = head_node
                    head = start_node
                    prev_node = end_node
                else:
                    end_node.next = prev_node.next
                    prev_node.next = start_node
                prev_node = end_node
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        return head
