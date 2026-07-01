class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row
        l = 0
        r = len(matrix)-1
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                if target <= matrix[mid][-1]:
                    l = mid
                    break
                l = mid + 1
            else:
                r = mid - 1
        row = l 
        print(l,r,row)
        l = 0
        r = len(matrix[row])-1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
                