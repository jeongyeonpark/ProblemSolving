"""class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return

        result = []
        q = deque([root])
        befor_pointer = root
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                node_val = node.val
                left_node = node.left
                right_node = node.right

                if node_val != None:
                    result.append(node_val)
                if left_node:
                    q.append(left_node)
                if right_node:
                    q.append(right_node)
                befor_pointer.next = node_val
                befor_pointer = node
            befor_pointer.next = "#"
        return root"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque()
        q.append(root)
        dummy=Node(-999) # to initialize with a not null prev
        print(dummy)
        while q:
            length=len(q) # find level length
            
            prev=dummy
            for _ in range(length): # iterate through all nodes in the same level
                popped=q.popleft()
                if popped.left:
                    q.append(popped.left)
                    prev.next=popped.left
                    prev=prev.next
                if popped.right:
                    q.append(popped.right)
                    prev.next=popped.right
                    prev=prev.next                
                 
        return root
