# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        sz = 0 
        real = head
        ans = head
        if(head.next is None and n == 1):
            head = None
            return head
        while(head.next.next is not None):
            sz += 1
            head = head.next     
        index = sz - n + 2
        while(index > 0):
            real = real.next
            index -= 1
        if(real.next is not None):
            real.val = real.next.val
            real.next = real.next.next
        else:
            head.next = None
        return ans
            