class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land = 0 
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    land += 1
                    q = [(x,y)]
                    grid[x][y] = "0"
                    #visited.add((x,y))
                    while q:
                        coor = q.pop()
                        for nc in [(coor[0]+1,coor[1]), (coor[0]-1,coor[1]), (coor[0],coor[1]+1), (coor[0],coor[1]-1)]:
                            if nc[0] >= 0 and nc[0] < len(grid) and nc[1] >= 0 and nc[1] < len(grid[0]):
                                if grid[nc[0]][nc[1]] == '1':
                                    q.append(nc)
                                grid[nc[0]][nc[1]] = "0"
                                #visited.add(nc)
        return land
