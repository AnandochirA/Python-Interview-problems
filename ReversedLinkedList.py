# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return head
        
        ans = None
        current = head
        
        while current is not None : 
            nextNode = current.next
            current.next = ans
            ans = current
            current = nextNode
        return ans