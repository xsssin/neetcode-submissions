class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        #while the part is sorted, there is a left and a right and a mid
        #usually the order should be left < mid < right
        #but what if left >mid?that means we have to move the right pointer to mid
        #what if right<mid?
        #that means we need to move left pointer to mid
        while l < r:
            mid = (l+r)//2

            if nums[l] >nums[mid]:
                r = mid
            
            elif nums[r] < nums[mid]:
                l = mid+1
            else:
                break
        

        return nums[l]
            


        