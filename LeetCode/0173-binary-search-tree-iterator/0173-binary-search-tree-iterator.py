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
            self.que.appendleft(self.curr_node.right)
            n_left = self.curr_node.right.left
            while n_left:
                self.que.appendleft(n_left)
                n_left = n_left.left
        return self.curr_node.val

    def hasNext(self) -> bool:
        return len(self.que) > 0
        


    # def __init__(self, root: TreeNode):
    #     self.stack = []
    #     self._leftmost_inorder(root)

    # # 왼쪽 자식들을 스택에 모두 넣음
    # def _leftmost_inorder(self, root):
    #     while root:
    #         self.stack.append(root)
    #         root = root.left

    # def next(self) -> int:
    #     # 스택의 최상단 요소가 다음 노드가 됨
    #     topmost_node = self.stack.pop()
        
    #     # 해당 노드의 오른쪽 자식이 있는 경우, 그 자식의 모든 왼쪽 자식을 스택에 추가
    #     if topmost_node.right:
    #         self._leftmost_inorder(topmost_node.right)
        
    #     return topmost_node.val

    # def hasNext(self) -> bool:
    #     return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()