class Solution:
    def search(self, nums: List[int], target: int) -> int:

      def binary_search(l, r):
        

        while l < r:
          mid = (l+r)//2
          if nums[mid] == target:
            return mid
          elif target > nums[mid]:
            l = mid +1
          else:
            r = mid

        return -1


      #find split
      l = 0
      r = len(nums)-1

      while l<r:
        mid = (l+r)//2
        if nums[mid] > nums[r]:
          l = mid+1
        else:
          r = mid
      
      pivot = l
      print(l)

      if nums[l]<= target <= nums[-1]:
        return binary_search(l, len(nums))
      else:
        return binary_search(0, l)
     
        

            

