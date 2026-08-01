class Trie:
    def __init__(self):
        self.chil = {}
        self.endOfWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.chil:
                cur.chil[c] =Trie()
            cur = cur.chil[c]

        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])


        res = set()

        def dfs(i, j, visited, root, curr):
            if root.endOfWord:
                res.add("".join(curr))
            

            
            if i>= ROWS or j>=COLS or i <0 or j<0 or (i,j) in visited:
                return
            
            if board[i][j] not in root.chil:
                return


            root = root.chil[board[i][j]]
            curr.append(board[i][j])
            visited.append((i,j))
                
            
            dfs(i+1, j, visited, root, curr) 
            dfs(i, j+1, visited, root, curr) 
            dfs(i-1, j, visited, root, curr) 
            dfs(i, j-1, visited, root, curr)

            visited.remove((i,j))
            curr.pop()
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i,j,[],root, [])
        return list(res)


                    


