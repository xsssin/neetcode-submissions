
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)



        def bt(i,subset ):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            #the choice to include nums[i]
            subset.append(nums[i])
            bt(i+1, subset)
            subset.pop()





            #the choice to not include nums[i]
            while i+1 <len(nums) and nums[i] == nums[i+1]:
                i+=1
            bt(i+1, subset)

        
        bt(0,[])

        return res
        
        
        