# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sum_leaf(node, n):
            n += node.val
            if n > targetSum:
                return False
            if n == targetSum:
                return True

            if node.right and node.left:
                return sum_leaf(node.right, n) or sum_leaf(node.left, n)
            elif node.right:
                return sum_leaf(node.right, n)
            elif node.left:
                return sum_leaf(node.left, n)

        if root:
            return sum_leaf(root,0)
        else:
            return False