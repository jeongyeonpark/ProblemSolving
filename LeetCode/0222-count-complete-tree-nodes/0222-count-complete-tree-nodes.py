# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        answer = 0
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                answer+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return answer

