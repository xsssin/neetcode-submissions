class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1map = [0]*26
        s2map = [0]*26
        matches = 0

        for i in s1:
            s1map[ord(i)-ord("a")] += 1

        for i in range(len(s1)):
            s2map[ord(s2[i])-ord("a")] += 1
        
        for i in range(26):
            if s2map[i] == s1map[i]:
                matches += 1

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # Add new character
            index = ord(s2[i]) - ord("a")
            s2map[index] += 1
            if s2map[index] == s1map[index]:
                matches += 1
            elif s2map[index] - 1 == s1map[index]:
                matches -= 1
            
            # Remove old character
            remove_idx = ord(s2[i - len(s1)]) - ord("a")
            s2map[remove_idx] -= 1
            if s2map[remove_idx] == s1map[remove_idx]:
                matches += 1
            elif s2map[remove_idx] + 1 == s1map[remove_idx]:
                matches -= 1
        
        return matches == 26