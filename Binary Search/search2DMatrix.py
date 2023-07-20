class Solution:
    #Time complexity: O(m + n) but we need O(log(m*n))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            print(matrix[r][c])
            if matrix[r][c] < target:        
                r += 1
            elif matrix[r][c] > target:
                c -= 1
            else: return True
        
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        topRow, bottomRow = 0, rows - 1
        
        while topRow <= bottomRow:
            mid = (topRow + bottomRow)//2
            if target > matrix[mid][-1]:
                topRow = mid + 1
            elif target < matrix[mid][0]:
                bottomRow = mid - 1
            else: 
                break
            
        if not topRow <= bottomRow:
            return False
        
        row = (topRow + bottomRow)//2
        left, right = 0, cols - 1
        
        while left <= right:
            m = (left + right)//2
            if target > matrix[row][m]:
                left = m + 1
            elif target < matrix[row][m]:
                right = m - 1
            else:
                return True
        
        return False