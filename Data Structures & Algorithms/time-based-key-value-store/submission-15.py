from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list) 
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([value, timestamp])
        #for key, value in self.timemap.items():
         #   print(f"{key}: {value}")
        
        

    def get(self, key: str, timestamp: int) -> str:
        #this is the value from the lastes entry
        #we have to find the largest timestamp that is smaller or equal to the imput timestamp
        #is the queue already sorted?
        #assuming that it is sorted, we will use binary search to find the number thhat is closest to the timestamp
        #how to represent the timestamp in the vzlues? -> self.timemap[key][insert index][1]

        l = 0
        r = len(self.timemap[key])-1
        res = ""



        if self.timemap[key] and timestamp < self.timemap[key][0][1] :
            #print(timestamp)
            #print(self.timemap[key][0][1] )
            #print(self.timemap[key][-1][1])
            return ""

        while l <= r:
            mid = (l+r)//2

            if timestamp == self.timemap[key][mid][1] :
                return self.timemap[key][mid][0]
            elif timestamp > self.timemap[key][mid][1]:
                res = self.timemap[key][mid][0]
                l = mid+1
            else:
                r = mid-1
        print("l is" + str(l))
        print("len of str -1 is" + str(len(self.timemap[key])-1))
        return res
            
        


        
