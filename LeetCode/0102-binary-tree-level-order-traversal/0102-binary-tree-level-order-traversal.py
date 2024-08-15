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

        nodes = []
        next_nodes = [root]

        while next_nodes:
            curr_nodes, next_nodes = next_nodes, []
            depth_nodes = []
    
            while len(curr_nodes)>0:
                curr_node = curr_nodes.pop(0)
                depth_nodes.append(curr_node.val)

                if curr_node.left  != None:
                    next_nodes.append(curr_node.left)
                if curr_node.right != None:
                    next_nodes.append(curr_node.right)
            nodes.append(depth_nodes)

        return nodes