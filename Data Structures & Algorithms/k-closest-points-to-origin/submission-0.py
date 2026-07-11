class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            dist = (x**2)+(y**2)
            min_heap.append([dist,x,y])

        heapq.heapify(min_heap)
        

        res = []

        while k >0:
            dist, x,y = heapq.heappop(min_heap)
            k -= 1
            res.append([x,y])


        return res

        