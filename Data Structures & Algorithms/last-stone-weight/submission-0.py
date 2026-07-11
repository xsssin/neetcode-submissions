class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >1:
            largest = abs(heapq.heappop(stones))
            large2 = abs(heapq.heappop(stones))
            if largest > large2:
                new = -(largest-large2)
                heapq.heappush(stones, new)

        stones.append(0)
        return abs(stones[0])
        