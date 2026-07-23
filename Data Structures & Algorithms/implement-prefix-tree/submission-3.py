class TrieNode:
    def __init__(self, val):
        self.val = val
        self.chil = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(0)

        

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.chil:
                root.chil[c] = TrieNode(c)
                
            root = root.chil[c]
        root.endOfWord = True
            


    def search(self, word: str) -> bool:

        root = self.root
        for c in word:
            if c not in root.chil:
                return False
            root = root.chil[c]
        
        return root.endOfWord

        
    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root.chil:
                return False
            root = root.chil[c]
        
        return True



        
        
        