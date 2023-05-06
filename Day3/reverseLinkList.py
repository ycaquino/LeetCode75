'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Ex.1
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Ex.2
Input: head = [1,2]
Output: [2,1]

Ex.3
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            prev_node = None
            curr_node = head
            next_node = head.next

            while next_node:
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
                next_node = next_node.next

            curr_node.next = prev_node

            return curr_node
        else:
            return None

def main():
    list1 = ListNode(1, None)
    curr = list1
    for num in [2, 3, 4, 5]:
        curr.next = ListNode(num, None)
        curr = curr.next

    print('Original List')
    curr = list1
    while curr:
        print(curr.val, end='')
        curr = curr.next
    print()

    reverse = Solution()

    print('Reversed List')
    list2 = reverse.reverseList(list1)
    curr = list2
    while curr:
        print(curr.val, end='')
        curr = curr.next




if __name__ == "__main__":
    main()