class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def bt(curr, front, back):
            if len(curr) == 2*n:
                res.append("".join(curr.copy()))
                return


            
            #the choice to add front
            if front < n:
                curr.append("(")

                bt(curr, front+1, back)
                curr.pop()
            

            #the choice to add back
            if back < front: #meaning we have nore( than )
                curr.append(")")

                bt(curr, front, back+1)
                curr.pop()
            
        

        bt([], 0,0)

        return res
