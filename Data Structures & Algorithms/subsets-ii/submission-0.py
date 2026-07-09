class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        res = []
        nums = sorted(nums)

        def bt(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            
            #the option to include nums[i]

            curr.append(nums[i])
            bt(i+1, curr)

            curr.pop()

            #the option to not include nums[i]
            while i +1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            bt(i+1, curr)
        
        bt(0,[])
        return res

        