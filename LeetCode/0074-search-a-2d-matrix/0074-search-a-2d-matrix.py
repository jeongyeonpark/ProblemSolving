class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x_len = len(matrix[0])
        y_len = len(matrix)

        for i in range(y_len):
            if target in matrix[i]:
                return True
            # if matrix[i][0]<=target and matrix[i][-1]>=target:
            # for j in range(x_len):
        return False
                