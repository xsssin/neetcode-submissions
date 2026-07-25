class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #phase 1:
        #create a fast and slow pointer to find the intersect
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        #phase2
        #create a new slow pointer and increment until they intersect
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break

        return slow
        