class Solution:
    def isValid(self, s: str) -> bool:

        p_map = {"}":"{", ")":"(", "]":"["}


        stack = []

        for i in s:
            if i in p_map:
                if stack and p_map[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)
        
        if len(stack) ==0:
            return True
        
        return False










        