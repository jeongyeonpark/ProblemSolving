# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def tree_list(curr_node, node_list, val):
            if curr_node is None:
                return None
            curr_val = curr_node.val
            node_list.append(curr_node)
            if curr_val == val:
                return node_list

            left_result = tree_list(curr_node.left, node_list[:], val)
            if left_result:
                return left_result

            right_result = tree_list(curr_node.right, node_list[:], val)
            if right_result:
                return right_result

            return None

        p_list = tree_list(root, [], p.val)
        q_list = tree_list(root, [], q.val)
        for i in range(min(len(p_list),len(q_list))-1, -1, -1):
            if p_list[i].val == q_list[i].val:
                return p_list[i]
