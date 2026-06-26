class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in board:
            vis = set()
            for j in i:
                if j == '.':
                    continue
                if j in vis:
                    return False
                vis.add(j)
        
        for i in range(9):
            vis = set()
            for j in range(9):
                val = board[j][i]
                if val == '.':
                    continue
                if val in vis:
                    return False
                vis.add(val)
        
        for i in range(3):
            for j in range(9):
                if j % 3 == 0:
                    vis = set()
                for k in range(i*3,i*3+3):
                    val = board[k][j]
                    if val == '.':
                        continue
                    print(val)
                    if val in vis:
                        return False
                    vis.add(val)
        return True
