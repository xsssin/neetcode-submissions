class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        ##create the leftmost node and the rightmost node
        self.left, self.right= Node(0,0), Node(0,0) #need to be written separately or they will be pointing at the same node they are just a mark and the key value doesn't really matters genuinely
        self.left.next = self.right 
        self.right.prev = self.left





    def remove(self, node):
        #to remove the node we would have to break the original links and
        #create new links

        #1. starting from the current node:
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev



    def insert(self, node):

        #basically we are inserting into the very right
        right = self.right
        prev = self.right.prev
        node.next = right
        right.prev = node
        prev.next = node
        node.prev = prev        

    def get(self, key: int) -> int:
        if key in self.cache:
            #since we called on the key now we have to move it 
            #to the very right

            #1. remove the node from the linked list
            self.remove(self.cache[key])
            #2.insert the node to the very right of the list
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #if it is already in cache, we just have to update its
            #value and also move the node to the very right of the linked list

            #we update it my making a new node

            self.remove(self.cache[key])
            #create new Node
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

        

        #if it is not in the cache we would need to insert it and 
        #evict the leftmost node ONLY iF the the capacity has been exceeded
        

        #1.create the new node
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if len(self.cache) > self.capacity:
                #evict LRU
                #which one is LRU? : its the one that is next to the leftmost node
                to_be_evicted = self.left.next
                self.remove(to_be_evicted)
                del self.cache[to_be_evicted.key]
        
        return
















        
