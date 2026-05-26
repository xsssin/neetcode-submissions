class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join(i.lower() for i in s if i.isalnum())

        left = 0
        right = len(new_s)-1
        while left<right:
            if new_s[left] != new_s[right]:
                return False
            left+=1
            right -=1 

        return True
            
        

        