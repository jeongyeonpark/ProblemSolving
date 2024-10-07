class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        start_x = 0
        start_y = 0
        end_x = len(grid[0])
        end_y = len(grid)

        q = deque([(0,0)])
        visited = set()
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                if not (x,y) in visited:
                    visited.add((x,y))
                    if x-1<0 and y-1<0:
                        pass
                    elif x-1<0 and y-1>=0:
                        grid[y][x] = grid[y][x]+grid[y-1][x]
                    elif x-1>=0 and y-1<0:
                        grid[y][x] = grid[y][x]+grid[y][x-1]
                    else: #x-1>= and y-1>=0
                        grid[y][x] = min(grid[y][x]+grid[y-1][x], grid[y][x]+grid[y][x-1])

                    if x+1<end_x:
                        q.append((x+1,y))
                    if y+1<end_y:
                        q.append((x,y+1))

        return grid[-1][-1]

