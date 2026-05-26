from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check row
        col = collections.defaultdict(set)
        row = collections.defaultdict(set)
        block = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in col[c] or board[r][c] in row[r] or board[r][c] in block[(r//3,c//3)]:
                        return False
                    else: 
                        col[c].add(board[r][c])
                        row[r].add(board[r][c])
                        block[(r//3,c//3)].add(board[r][c])


        
        return True

                         


 



            










        

    





            









        