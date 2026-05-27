class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []

        for i, v in enumerate(sorted_nums):
            if i > 0:
                if v == sorted_nums[i-1]:
                    continue
            
            left = i+1
            right = len(sorted_nums)-1

            while left < right:
                if v + sorted_nums[left]+ sorted_nums[right] == 0:
                    res.append([v,sorted_nums[left],sorted_nums[right]])
                    left += 1
                    while sorted_nums[left] == sorted_nums[left-1] and left < right:
                        left += 1

                elif v + sorted_nums[left]+ sorted_nums[right] > 0:
                    right -=1
                
                else: 
                    left += 1
        
        return res
                
                




        


           