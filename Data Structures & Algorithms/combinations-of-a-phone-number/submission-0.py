class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        if not digits:
            return []
        res = []


        def bt(i,  curr):
            if i == len(digits):
                res.append("".join(curr.copy()))
                return
            

            #the choice to add every element from i+1
            for j in range(len(digit_map[digits[i]])):
                curr.append(digit_map[digits[i]][j])
                bt(i+1,curr)
                curr.pop()
            
        

        bt(0,[])
        return res
            


