class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []


        def bt(i, curr,total):
            if i >= len(nums) or total> target:
                return
            if total == target:
                res.append(curr.copy())
                return
            

            #the option to include nums[i]
            curr.append(nums[i])
            bt(i, curr, total+ nums[i])
            curr.pop()



            #the option to not include nums[i]
            bt(i+1, curr, total)

            return curr
        
        bt(0,[],0)

        return res


        
        