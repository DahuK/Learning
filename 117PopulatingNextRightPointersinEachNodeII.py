'''
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
'''

class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return
        first_node = None
        if root.left:
            first_node = root.left
        if root.right:
            if first_node:
                root.left.next = root.right
            else:  
                first_node = root.right
           
        while first_node:
            next_first_node = None
            cur_node = None
            node = first_node
            while node :
                if node.left:
                    if cur_node:
                        cur_node.next = node.left
                    else:
                        next_first_node = node.left
                    cur_node = node.left
                if node.right:
                    if cur_node:
                        cur_node.next = node.right
                    else:
                        next_first_node = node.right
                    cur_node = node.right
                node = node.next
            first_node = next_first_node
        
if __name__ == '__main__':
    
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n7 = TreeLinkNode(7)
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n7
    
    s = Solution()
    s.connect(n1)
    
    print n5.next.val
    pass