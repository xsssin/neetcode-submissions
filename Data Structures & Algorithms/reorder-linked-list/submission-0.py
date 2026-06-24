# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #step1： find the mid point

        #use the slow and fast
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #step2: reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first = head
        second = prev
        #step3: stich the two halves
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2







        