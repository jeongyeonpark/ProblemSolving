# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_num = 0
        num = ''
        def cal(node, num):
            nonlocal sum_num
            if node:
                num +=str(node.val)
            else:
                return

            if not node.left and not node.right:
                sum_num+=int(num)
            else:
                cal(node.left, num)
                cal(node.right, num)
            
        cal(root, num)
        return sum_num
        