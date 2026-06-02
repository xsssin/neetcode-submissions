class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #there are m rows
        #there are n colums
        #which means the very middle is matrix[(rl+rr)//2][(cl+cr)//2]


        #if the current row is r and the current column is 
        #i think we shoud first start from narrowing down the rows by putting the first and last number
        #of each row.after narrowing down the rows we can start narrowing within a row
        

        #we should start from the very middle row? but which? the first number or last number? I guess it
        #doesn't even matter. 
        #maybe start from the first number then

        #row_pointer

        row_l = 0
        row_r = len(matrix)-1

        col_l = 0
        col_r = len(matrix[0])-1

        while row_l <= row_r:
            row = (row_l+row_r)//2
            if target > matrix[row][-1]  :
                row_l = row+1
            elif target < matrix[row][0]:
                row_r = row-1
            else:
                break
        
        if not row_l <= row_r:
            return False
        row = (row_l+row_r)//2
        while col_l <= col_r:
            col = (col_l+col_r)//2
            if matrix[row][col] > target:
                col_r = col -1

            elif matrix[row][col] < target:
                col_l = col+1
            else:
                return True
            
        
        return False


            



        