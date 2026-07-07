# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1


        dummy = ListNode()
        new_head = dummy

        head1 = list1
        head2 = list2


        while head1 and head2:
            if head1.val <= head2.val:
                new_head.next = head1
                head1 = head1.next
            else:
                new_head.next = head2
                head2 = head2.next

            new_head = new_head.next


        if head1:
            new_head.next = head1
        if head2:
            new_head.next = head2
        

        return dummy.next

        