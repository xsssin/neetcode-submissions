# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        #now the beginning of the second part is slow.next
        second_current = slow.next
        slow.next =None
        #now do the whole reverse list thing 4 steps:
        prev = None
        while second_current:
            temp = second_current.next
            second_current.next = prev
            prev = second_current
            second_current = temp

        


        #lastly, stich the two lists
        #how do I do this again?

        #since we are making sure the fisrt half is always shorter we can always link the
        #remaining of the second to the first half
        second = prev
        first = head
        while second:
            first_temp = first.next
            second_temp = second.next

            first.next = second
            second.next = first_temp

            first = first_temp
            second = second_temp

    
        return 

