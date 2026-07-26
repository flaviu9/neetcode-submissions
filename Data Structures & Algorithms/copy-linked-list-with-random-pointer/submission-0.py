"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.hmap = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        if curr == None:
            return None
        
        if curr in self.hmap:
            return self.hmap[curr]
        
        copy = Node(curr.val)
        self.hmap[curr] = copy

        copy.next = self.copyRandomList(curr.next)
        copy.random = self.copyRandomList(curr.random)

        return copy
