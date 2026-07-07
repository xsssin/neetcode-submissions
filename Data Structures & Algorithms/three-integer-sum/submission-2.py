class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        sorted_nums = sorted(nums)


        for a_pointer in range(len(nums)):
            if a_pointer >= 1 and sorted_nums[a_pointer] == sorted_nums[a_pointer-1]:
                continue
            else:

                negative_a = -sorted_nums[a_pointer]

                #initialize l and r
                l = a_pointer+1
                r = len(nums)-1

                while l<r:
                    b = sorted_nums[l]
                    c = sorted_nums[r]

                    if b+ c == negative_a :
                        res.append([sorted_nums[a_pointer], b,c])
                        l+= 1

                        while l < r and sorted_nums[l] == sorted_nums[l-1]:
                            l += 1
                    elif b +c > negative_a:
                        r -=1
                    else:
                        l += 1
                        
                
        
        return res


