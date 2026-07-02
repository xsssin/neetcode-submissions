class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #what data structure would you use for checking duplicated?
        #Honestly I would use a set....and if it hits the anything in the set just return false


        
        #check row 
        for i in range(9):
            dup_set_row = set()
            dup_set_col = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in dup_set_row:
                        return False
                    dup_set_row.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in dup_set_col:
                        return False
            
                    dup_set_col.add(board[j][i])


        #check square
        dup_dic_square = {}  #{[0,0]:()} the key is the square, the value is the set
        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current != ".":
                    square = (i//3, j//3)
                    if square in dup_dic_square:
                        if current in dup_dic_square[square]:
                            return False
                        else:
                            dup_dic_square[square].add(current)
                    else:
                        dup_dic_square[square] = {current}

        

        return True


       

        



        return False





        