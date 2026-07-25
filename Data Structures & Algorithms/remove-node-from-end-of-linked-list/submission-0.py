# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ls = []
        curr = head
        while curr:
            ls.append(curr.next)
            curr = curr.next
        
        idx = len(ls) - n

        if idx == 0:
            return head.next
        else:
            ls[idx - 1].next = ls[idx].next
        
        return head
        
        