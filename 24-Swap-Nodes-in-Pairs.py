# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        \\\
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        \\\
        #Tracking Variables

        temp = head
        before = None 
        length = 0

        while temp:
            length += 1
            if length % 2 == 0 and length > 0:
                box = temp.val
                temp.val = before.val
                before.val = box

            before = temp
            temp = temp.next
            
        

        return head
            