class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {} #stores the key and the actual key pair
        self.capacity = capacity
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        #the lru is the one that is on the right to the left
        #when inserting we insert it to the left of the right

        #we need to connect the node
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache_dict:
            self.remove(self.cache_dict[key])
            self.insert(self.cache_dict[key])
            return self.cache_dict[key].val
        return -1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    


    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node 


    def put(self, key: int, value: int) -> None:
        if key in self.cache_dict:
            node = self.cache_dict[key]
            node.val = value
            self.remove(node)
            self.insert(node)

        else:
            if len(self.cache_dict) >= self.capacity:
                lru = self.left.next
                self.remove(lru)
                del self.cache_dict[lru.key]

            new_node = ListNode(key, value)
            self.cache_dict[key] = new_node
            self.insert(new_node)



        


        
