# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head                  # pointer to traverse the list

        while curr and curr.next != None:    # ensure current and next node exist
            if curr.val == curr.next.val:
                # duplicate found → skip next node
                curr.next = curr.next.next
            else:
                # values different → move forward
                curr = curr.next

        return head                  # return modified list
        