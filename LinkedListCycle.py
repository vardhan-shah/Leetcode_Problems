# Problem Link: https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return
        try:
            slow = head
            fast = head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
