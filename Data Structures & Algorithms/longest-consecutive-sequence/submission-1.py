class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        print(sorted_nums)

        current_length = 1
        max_length = 1

        if nums ==[]:
            return 0




        prev = sorted_nums[0]
        for i in range(1,len(nums)):
            prev = sorted_nums[i-1]
            if sorted_nums[i] - sorted_nums[i-1] == 1:
                current_length += 1
                max_length = max(max_length, current_length)
            elif sorted_nums[i] - sorted_nums[i-1] == 0:
                continue
            else:
                current_length = 1
                max_length = max(max_length, current_length)
        
        return max_length
                
            


        