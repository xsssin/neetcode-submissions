from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        res = []

        count = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1

        sorted_freq = dict(sorted(freq.items(), key = lambda x:x[1], reverse = True))

        res.extend(list(sorted_freq.keys())[:k])

        
        

        
        return res
