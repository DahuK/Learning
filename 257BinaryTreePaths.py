'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        
        res = []
        if root is None:
            return res
        node = root
        self.trace_child(node, res, None)
        return res
            
    def trace_child(self, node, res, path):
        if node is not None:
            path = path + '->' + str(node.val) if path is not None else str(node.val)
        l_node = node.left
        r_node = node.right
        if l_node is None and r_node is None:
            res.append(path)
            return
        if l_node is not None:
            self.trace_child(l_node, res, path)
        if r_node is not None: 
            self.trace_child(r_node, res, path)
            
            
#    def get_children(self, node):`
        
if __name__ == '__main__': 
    t1 = TreeNode(1) 
    t2 = TreeNode(2) 
#    t3 = TreeNode(3) 
#    t4 = TreeNode(5) 
    t1.left = t2
#    t1.right = t3
#    t2.right = t4
    
    s = Solution()
    print s.binaryTreePaths(t1)
    
    