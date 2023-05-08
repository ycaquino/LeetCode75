'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Ex.1
Input: head = [1,2,3,4,5]
Output: [3,4,5]

Ex.2
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        if head:
            curr = head
            length = 0

            while curr:
                length += 1
                curr = curr.next

            mid = (length / 2 if length % 2 != 0 else length / 2 + 1) - 1

            curr = head
            count = 0

            while count < mid:
                count += 1
                curr = curr.next

            return curr

        else:
            return None