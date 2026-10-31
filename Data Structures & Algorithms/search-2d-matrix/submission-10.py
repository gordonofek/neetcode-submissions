class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        left = 0
        right = (m * n) - 1 #2

        while left<=right:
            mid = (left+right)//2 #1
            row = mid//m #0
            column = mid%m #1
            current = matrix[row][column]
            if current < target:
                left = mid+1
            elif current > target:
                right = mid-1
            else:
                return True

        return False

        