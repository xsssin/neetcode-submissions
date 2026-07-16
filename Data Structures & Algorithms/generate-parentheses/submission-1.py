class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def bt(cur, front, back):
            if len(cur) == 2*n:
                res.append("".join(cur.copy()))
                return
            
            #the choice to include front
            if front < n:
                cur.append("(")

                bt(cur,front+1, back)
                cur.pop()
            

            #the choice to not include back
            if back < front:
                cur.append(")")
                bt(cur, front, back+1)
                cur.pop()

        

        bt([],0,0)
        return res

        