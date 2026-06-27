# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head acts as a placeholder to simplify list creation
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        # Loop while there are nodes to process or a carry remaining
        while l1 or l2 or carry:
            # Extract values, default to 0 if list reached its end
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position
            total = val1 + val2 + carry
            
            # Update carry and calculate the digit to store
            carry = total // 10
            digit = total % 10
            
            # Create new node and move the cursor forward
            curr.next = ListNode(digit)
            curr = curr.next
            
            # Advance the list pointers if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # The actual result starts from the node after the dummy head
        return dummy_head.next