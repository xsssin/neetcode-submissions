class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        
        


        def dfs(curr, first_count, second_count):
            if first_count == n and second_count == n:
                res.append("".join(curr))
                return

            if first_count > n or second_count>n:
                return
            
            if first_count < n:
                curr.append("(")
                dfs(curr, first_count +1, second_count)
                curr.pop()

            if second_count < first_count:
                curr.append(")")
                dfs(curr, first_count, second_count+1)
                curr.pop()

        

        dfs([],0,0)
        return res
            
            

        