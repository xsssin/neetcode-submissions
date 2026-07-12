class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        min_heap = []

        for  i in range(k):
            min_heap.append(nums[i])

        heapq.heapify(min_heap)
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heapreplace(min_heap, nums[i])
        

        return min_heap[0]