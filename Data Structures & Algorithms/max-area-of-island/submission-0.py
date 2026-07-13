from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #edge case
        if not grid:
            return 0

        
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0


        def bfs(r,c):
            cur = 1
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r = dr +r
                    new_c = dc +c
                    if (new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1 and (new_r, new_c) not in visit):
                        q.append((new_r,new_c))
                        visit.add((new_r, new_c))
                        cur +=1
            
            return cur



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    max_area= max(max_area, bfs(r,c))

                
        
        return max_area

        