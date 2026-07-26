class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []


        def bt(i, curr):
            #base case
            if i == len(nums):
                res.append(curr.copy())
                return
            
            

            #the choice to include nums[i]
            curr.append(nums[i])
            bt(i+1, curr)
            curr.pop()


            #the choice to not include nums[i]
            bt(i+1, curr)

            return curr
        
        bt(0,[])


        return res

        