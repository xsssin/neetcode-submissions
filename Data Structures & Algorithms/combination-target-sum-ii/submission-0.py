class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates.sort()

        def bt(i, cur,total):

            if total == target:
                res.append(cur.copy())
                return

            if total> target or i == len(candidates):
                return
             

            #the choice to include the number candidates[i]
            cur.append(candidates[i])
            bt(i+1, cur, total+ candidates[i])
            cur.pop()
            #the choice to not include the number candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            
            bt(i+1, cur, total)

        bt(0,[],0)
        return res        