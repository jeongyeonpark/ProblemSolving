# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        v_list = []
        q = deque([root])
        min_v = 10**5

        while q:
            curr_node = q.popleft()
            if curr_node.val in v_list:
                return 0
            else:
                if len(v_list) > 2:
                    v = curr_node.val
                    v_list = sorted(v_list)

                    if v < v_list[0]:
                        min_v = min(abs(v - v_list[0]), min_v)
                    elif v > v_list[-1]:
                        min_v = min(abs(v - v_list[-1]), min_v)
                    else:
                        for i in range(len(v_list)-1):
                            if v>v_list[i] and v<v_list[i+1]:
                                min_v_ = min(abs(v - v_list[i]), abs(v - v_list[i+1]))
                                min_v = min(min_v_, min_v)

                else:
                    for v in v_list:
                        min_v = min(abs(curr_node.val - v), min_v)

                v_list.append(curr_node.val)
            
            if curr_node.left:
                q.append(curr_node.left)

            if curr_node.right:
                q.append(curr_node.right)
        return min_v