
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        arr = [-1] * (n * n)
        index = 0
        for i in range(n-1, -1, -1):
            row = board[i] if (n - i) % 2 != 0 else board[i][::-1]
            for value in row:
                arr[index] = value
                index += 1

        queue = deque([(0, 0)])  # (curr_position, step_count)
        visited = set([0])

        while queue:
            idx, moves = queue.popleft()
            if idx == n * n - 1:  
                return moves

            for i in range(1, 7):  
                next_idx = idx + i
                if next_idx >= n * n:
                    break

                if arr[next_idx] != -1:
                    next_idx = arr[next_idx] - 1

                if next_idx not in visited:
                    visited.add(next_idx)
                    queue.append((next_idx, moves + 1))

        return -1 
