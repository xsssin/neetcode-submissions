class MedianFinder:

    def __init__(self):
        self.small= []
        self.large = []

        

    def addNum(self, num: int) -> None:
        #always add the number to small
        heapq.heappush(self.small, -1*num)


        #1. check if the number we just added is larger than large
        if (self.small and self.large and -1* self.small[0]> self.large[0]):
            popped = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*popped)

        #2. check if they are approaximately the same len
        if(len(self.small) > len(self.large)+1 ):#small is larger
            popped = heapq.heappop(self.small)
            heapq.heappush(self.large, -1*popped)
        elif (len(self.large)> len(self.small)+1):
            popped=heapq.heappop(self.large)
            heapq.heappush(self.small, -1*popped)



    def findMedian(self) -> float:
        if len(self.small)== len(self.large):
            small_pop = -1*self.small[0]
            large_pop = self.large[0]

            return (small_pop+large_pop)/2
        elif len(self.small)>len(self.large):
            return -1*self.small[0]
        else:
            return self.large[0]








