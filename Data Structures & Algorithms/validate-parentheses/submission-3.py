class Solution:
    def isValid(self, s: str) -> bool:
        mymap = {")":"(", "}":"{", "]":"["}


        stack = []

        for i in s:
            if i in mymap:
                top_element = stack.pop() if stack else "#"

                if mymap[i] != top_element:
                    return False
            
            else:
                stack.append(i)
        
        if stack == []:
            return True

        return False        