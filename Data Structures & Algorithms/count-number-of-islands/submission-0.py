from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        #initializations
        island = 0
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    new_row = r+dr
                    new_col = c + dc
                    if (new_row) in range(ROWS) and (new_col) in range(COLS) and  grid[new_row][new_col] == '1' and (new_row, new_col) not in visit:
                       q.append((new_row, new_col))
                       visit.add((new_row, new_col))                       


                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] =="1" and (r,c) not in visit:
                    bfs(r,c)
                    island +=1
        
        return island

        