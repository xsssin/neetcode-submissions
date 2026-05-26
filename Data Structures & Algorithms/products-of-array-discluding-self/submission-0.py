class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        for i in range(len(nums)):
            new_list = nums[:i] + nums[i+1:]

            product = 1
            for j in range (len(new_list)):
                product *= new_list[j]

            res.append(product)

        return res