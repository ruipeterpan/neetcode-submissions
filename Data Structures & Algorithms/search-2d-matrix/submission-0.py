class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2

            r = mid // n
            c = mid % n   
            # r, c = divmod(mid, n)
            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            elif target < val:
                right = mid - 1
        
        return False


