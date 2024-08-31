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
        self.curr_node = self.que.popleft()
        if self.curr_node.right:
            n = self.curr_node.right
            self.que.appendleft(n)
            n_left = n.left
            if n_left:
                while n_left:
                    self.que.appendleft(n_left)
                    n_left = n_left.left
        return self.curr_node.val

    def hasNext(self) -> bool:
        if len(self.que) < 1:
            return False
        return True
        # if len(self.que) > 0:
        #     return True
        # next_node = self.que.popleft()
        # self.que.appendleft(next_node)
        # if self.curr_node.val < next_node.val:
        #     return True
        # return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()