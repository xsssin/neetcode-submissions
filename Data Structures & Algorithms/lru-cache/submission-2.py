class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0,0)
        self. right= Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity

        self.kv_map = {} #we are actually storing the key :key value

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key not in self.kv_map:
            return -1

        #move it to the very right
        self.remove(self.kv_map[key])
        self.insert(self.kv_map[key])
        return self.kv_map[key].val
      
        

    def put(self, key: int, value: int) -> None:
        if key in self.kv_map:
            node = self.kv_map[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            

        else:
            new = Node(key, value)
            self.kv_map[key] = new
            self.insert(new)
            if len(self.kv_map) > self.capacity:
                #evict the one at the very end
                #remove the one next to left
                lru = self.left.next
                self.remove(self.left.next)
                del self.kv_map[lru.key]
            



        
