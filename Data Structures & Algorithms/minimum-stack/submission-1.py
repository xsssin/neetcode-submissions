class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] #actually store the index instead of the value
        

    def push(self, val: int) -> None:
        self.stack.append(val)
    
        if not self.min_stack:
            self.min_stack.append(len(self.stack)-1) #store the index of the value. Since it 
            #is the last one pushed it should be the len of the stack-1
        else:
            if val < self.stack[self.min_stack[-1]]:
                self.min_stack.append(len(self.stack)-1)

    def pop(self) -> None:
        if len(self.stack)-1 == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        print(self.min_stack[-1])
        return self.stack[self.min_stack[-1]]

        
