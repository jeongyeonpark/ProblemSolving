# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_len = 0
        l2_len = 0
        over = 0

        node1 = l1
        node2 = l2

        num = 0
        if node1:
            num+=int(node1.val)
            l1_len+=1
        if node2:
            num+=int(node2.val)
            l2_len+=1
        num += over

        if num >= 10:
            over = 1
            num-=10
        else:
            over = 0
        if node1:
            node1.val = num
        if node2:
            node2.val = num

        while node1.next!= None or node2.next != None:
            num = 0
            if node1.next:
                node1 = node1.next
                num+=int(node1.val)
                l1_len+=1
            if node2.next:
                node2 = node2.next
                num+=int(node2.val)
                l2_len+=1
            num += over

            if num >= 10:
                over = 1
                num-=10
            else:
                over = 0

            if node1:
                node1.val = num
            if node2:
                node2.val = num
                
        if l1_len >= l2_len:
            if over == 1:
                node1.next = ListNode(1, None)
            return l1
        else:
            if over == 1:
                node2.next = ListNode(1, None)
            return l2