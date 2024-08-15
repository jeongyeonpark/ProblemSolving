# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        nodes = [root]
        while nodes:
            depth_nodes = []
            for _ in range(len(nodes)):
                curr_node = nodes.pop(0)
                depth_nodes.append(curr_node.val)

                if curr_node.left:
                    nodes.append(curr_node.left)
                if curr_node.right:
                    nodes.append(curr_node.right)
            result.append(depth_nodes)

        return result