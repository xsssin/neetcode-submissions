class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []


        board = [["."]*n for i in range(n)]

        def bt(row, col, pos_diag, neg_diag):
            if row == n:
                res.append(["".join(row) for row in board])

            
            for c in range(n):
                if c in col or (row+c) in pos_diag or (row-c) in neg_diag:
                    continue
                
                else:
                    board[row][c] = "Q"
                    col.add(c)
                    pos_diag.add(row+c)
                    neg_diag.add(row-c)

                    bt(row+1, col, pos_diag, neg_diag)


                    board[row][c] = "."
                    col.remove(c)
                    pos_diag.remove(row+c)
                    neg_diag.remove(row-c)

        bt(0, set(), set(), set())

        return res

                    
                
        