# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2 sorted linked lists, merge them into one sorted list and return head of the sorted linked list
        output should be made up of the nodes from l1 and l2

        check which head is smaller and set it as the head, check which element 
        is smaller between the next of the current head and the head of the other linked list
        if next of curr of l1 is less, set val as next
        if head of l2 is less, save l1 next for later to use it for comparison and set the next for l1 to the head of l2
        check prev_next_l1 is less than l1 head next, save head next as prev_next_l1 and set next head l1 to prev_next_l1
        """

        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

