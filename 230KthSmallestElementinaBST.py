'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        s_list = []
        self.trace_tree(root, s_list, k)
        kth_node = s_list.pop()
        return kth_node.val
    
    def trace_tree(self, node, s_list, k):

        if node.left is not None:
            self.trace_tree(node.left, s_list, k)
        if len(s_list) is k:
            return
        s_list.append(node)
        if node.right is not None:
            self.trace_tree(node.right, s_list, k)
        
        
if __name__ == '__main__':
    r = TreeNode(8)
    
    n1 = TreeNode(1) 
    n2 = TreeNode(3) 
    n3 = TreeNode(5) 
    n4 = TreeNode(7) 
    n5 = TreeNode(9)
    n6 = TreeNode(10)
    
    n2.left = n1
    n3.left = n2
    n3.right = n4
    r.left = n3
    r.right = n6
    n6.left = n5
    
    s = Solution()
    k = 3
    print s.kthSmallest(r, k)
    
    pass