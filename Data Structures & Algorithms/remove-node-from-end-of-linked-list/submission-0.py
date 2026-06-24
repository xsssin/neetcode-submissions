# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)


        end_pointer = dummy
        prev = dummy
        
        #step one: find the nth element
        for _ in range(n+1):
            end_pointer = end_pointer.next

        

        while end_pointer:
            prev = prev.next
            end_pointer = end_pointer.next
        

        prev.next = prev.next.next

        return dummy.next





        