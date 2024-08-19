class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0 and not (row,col) in visited:
                    visited.add((row,col))

                    for r in range(rows):
                        if not matrix[r][col] == 0:
                            matrix[r][col] = 0
                            visited.add((r,col))

                    for c in range(cols):
                        if not matrix[row][c] == 0:
                            matrix[row][c] = 0
                            visited.add((row,c))
        return matrix
