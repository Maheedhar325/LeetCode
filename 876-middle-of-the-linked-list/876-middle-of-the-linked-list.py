# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head
        # idx = 1
        # while temp:
        #     temp = temp.next
        #     idx+=1
        # cur = head
        # for i in range(1,idx//2):
        #     cur = cur.next
        # return cur if idx%2==0 else cur.next
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

            
        