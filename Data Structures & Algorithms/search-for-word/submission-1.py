class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROW = len(board)
        COL = len(board[0])


        def dfs(i,j, idx, visited):
            if idx == len(word):
                return True
            
            if i >= ROW or i<0 or j>=COL or j<0 or (i,j)in visited:
                return False
            
            if board[i][j] != word[idx]:
                return False

            visited.add((i,j))
            found = dfs(i+1, j, idx+1, visited) or dfs(i, j+1, idx+1, visited)or dfs(i, j-1, idx+1, visited) or dfs(i-1, j, idx+1, visited)
            visited.remove((i,j))
            return found
            
            
            
        
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if dfs(r,c,0,set()):
                        return True
        

        return False


            



            
        