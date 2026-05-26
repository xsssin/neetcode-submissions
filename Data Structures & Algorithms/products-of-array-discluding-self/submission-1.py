class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1]*len(nums)

        prefix = 1 
        for i in range(len(nums)):
            resi_copy = nums[i]

            res[i] *= prefix
            prefix *= resi_copy

        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            resj_copy = nums[j]

            res[j] *= postfix
            postfix *= resj_copy


        return res


        



            


