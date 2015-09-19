'''
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
'''

#Definition for binary tree with next pointer.
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
        nodes_stack = []
        if root.left:
            nodes_stack.append(root.left)
        if root.right:
            nodes_stack.append(root.right)
            root.left.next = root.right
        
        while nodes_stack:
            next_level_stack = []
            
            cur_node = None
            for node in nodes_stack:
                if node.left:
                    if cur_node:
                        cur_node.next = node.left
                    cur_node = node.left
                    next_level_stack.append(cur_node)
                if node.right:
                    cur_node.next = node.right
                    cur_node = node.right
                    next_level_stack.append(cur_node)
            
            nodes_stack = next_level_stack
        
        
if __name__ == '__main__':
    
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    
    n1.left = n2
    n1.right = n3
    
    s = Solution()
    s.connect(n1)
    
    print n2.next.val
    pass