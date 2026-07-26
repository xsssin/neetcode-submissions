class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        already_visited = {}
        def dfs(r,c):
            if r>=m or c>=n:
                return 0
            
            if r== m-1 or c == n-1:
                return 1
            
            if (r,c) in already_visited:
                return already_visited[(r,c)]

            
            count = 0
            count += dfs(r, c+1)
            count += dfs(r+1, c)

            already_visited[(r,c)] =  count
            return count
        
        return dfs(0,0)
       



        