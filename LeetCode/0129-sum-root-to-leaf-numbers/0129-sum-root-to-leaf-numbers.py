# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        sum_num = 0
        num = 0
        def cal(node, num):
            nonlocal sum_num
            if node:
                #num +=str(node.val)
                num = num*10+node.val
            else:
                return

            if not node.left and not node.right:
                sum_num+=int(num)
            else:
                cal(node.left, num)
                cal(node.right, num)
            
        cal(root, num)
        return sum_num
        