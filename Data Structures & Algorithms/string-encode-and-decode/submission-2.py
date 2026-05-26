class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for i in range(len(strs)):
            count  = len(strs[i])
            encoded += str(count) + "#"+strs[i] 


        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        current_index = 0

        while current_index < len(s):

            number_index = current_index
            while s[number_index] != "#":
                number_index += 1
            
            size = int(s[current_index:number_index])

            decoded.append(s[number_index+1:number_index + size+1])

            current_index += len(s[current_index:number_index])+1+size
        
            



        return decoded

