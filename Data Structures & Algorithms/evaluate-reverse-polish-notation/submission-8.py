class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+","-","*","/"}


        stack = []


        for i in tokens:
            if i in operands:
                r = int(stack.pop())
                l = int(stack.pop())

                if i == "+":
                    res = r +l
                elif i == "-":
                    res = l -r
                elif i == "*":
                    res = r*l
                elif i == "/":
                    res = int(l/r)
                
                stack.append(res)
            else:
                stack.append(int(i))
            
        
        return stack[0]

        