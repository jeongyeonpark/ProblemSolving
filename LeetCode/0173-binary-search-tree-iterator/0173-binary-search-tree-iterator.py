# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.que = deque([root])
        node = root.left
        while node:
            self.que.appendleft(node)
            node = node.left

    def next(self) -> int:
        curr_node = self.que.popleft()
        right = curr_node.right
        while right:
            self.que.appendleft(right)
            right = right.left
        return curr_node.val

    def hasNext(self) -> bool:
        return len(self.que) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()