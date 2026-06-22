class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix) , len(matrix[0])
        n = rows * cols 
        for i in range(n):
            row = i // cols
            col = i % cols  
            if matrix[row][col] == target:
                return True
        return False        