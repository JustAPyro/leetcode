from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        This is a pretty classic one. We're going to combine these lists by comparing the head nodes
        in order and then adding them to the new list.

        Edit 1: I think i'm actually going to implement a make_list method so that
        I can test some variations of solutions while I'm working

        Edit2: I think maybe I can do this recursively! But after trying for a bit I
        don't think I can without changing the method signature.

        Edit3: This is tricky. I'm going to try thinking of it as returning list 1 and
        work on parsing list 2 "into" list one.
        '''
        # Handle edge cases where one or both is none
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        # At this point we know we have two elements
        # so we pick the smallest to start a new chain
        head: ListNode = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        tail: ListNode = head

        # Now we just add the smallest from either side
        while (list2 != None or list1 != None):
            # If we've reached the end on either side just
            # toss on the rest and return
            if list1 == None:
                tail.next = list2
                return head
            elif list2 == None:
                tail.next = list1
                return head

            if list1.val <= list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            elif list2.val <= list1.val:
                tail.next = list2
                tail = list2
                list2 = list2.next
        return head

def make_list(*nums: List[int]) -> List[ListNode]:
    head = None
    last = None
    for num in nums:
        new_node = ListNode(num)
        if last:
            last.next = new_node
            last = new_node
        else:
            last = new_node
            head = new_node
    return head

def print_list(head):
    while head != None:
        print(head.val)
        head = head.next

s = Solution()
result = s.mergeTwoLists(
    make_list(1, 2, 4),
    make_list(1, 3, 4)
)

print_list(result)
