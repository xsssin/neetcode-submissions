class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        count = 0
        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return 0
            
            if total == amount:
               
                return 1

            
            if (i, total) in dp:
                return dp[(i, total)]

            
            include = dfs(i, total+coins[i])

            exclude = dfs(i+1, total)


            dp[(i, total)] = include+ exclude

            return dp[(i,total)]

        
        return dfs(0,0)



            