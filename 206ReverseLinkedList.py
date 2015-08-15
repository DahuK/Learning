'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        node = head
        head = head.next
        node.next = None
        while head:
            prev = node
            node = head
            head = head.next
            node.next = prev
     
        return node
    
    
#    public ListNode reverseList(ListNode head) {
#   return reverseList(head, null);
#    }
#
#    private ListNode reverseList(ListNode head, ListNode prev) {
#        if(head == null){
#            return prev;
#        }else{
#            ListNode next= head.next;
#            head.next = prev;
#            return reverseList(next, head);
#        }
#    }

if __name__ == '__main__':
    
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    s = Solution()
    nl = s.reverseList(l1)
    
    while nl:
        print str(nl.val)
        nl = nl.next
    
    pass