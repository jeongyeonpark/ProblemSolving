# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution_jy:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr_node = head
        min_node = head

        q = deque([head])
        #print(q)
        while q:
            curr_node = q.pop()
            prev_node = None

            if curr_node.next:
                next_node = curr_node.next

                while curr_node.val > next_node.val:
                    q.append(next_node)
                    if min_node.val > next_node.val:
                        min_node = next_node

                    curr_node.next = next_node.next
                    next_node.next = curr_node

                    if prev_node:
                        prev_node.next = next_node
                    prev_node = next_node

                    if next_node == None:
                        break
        return min_node

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Split the linked list into two halves using "slow and fast pointer" technique to find the midpoint of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # The midpoint of the linked list is slow.next
        mid = slow.next
        # Set slow.next to None to separate the left and right halves of the linked list
        slow.next = None

        # Recursively sort the left and right halves of the linked list
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves of the linked list
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        # Append the remaining nodes of the left or right half to the end of the sorted list
        curr.next = left or right

        return dummy.next