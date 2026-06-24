"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        node_map = {None: None}

        #first iteration is just to create copy of the nodes without linking them
        while curr:
            copy = Node(curr.val) #parse in the value of the node
            node_map[curr] = copy
            curr = curr.next
        

        #second itertion is to actually fill in the copy of the nodes
        curr = head
        while curr:
            copy = node_map[curr]
            copy.next = node_map[curr.next]
            copy.random = node_map[curr.random]
            curr = curr.next
        
        return node_map[head]

