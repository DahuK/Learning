'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def getHeight(self, root):
        count = 0 
        while root:
            count +=1
            root = root.left
        return count
    
    def countNodes(self, root):
        if root is None:
            return 0     
        h = self.getHeight(root.left)
        h_r = self.getHeight(root.right)
        if h == h_r:
            return 2 ** h + self.countNodes(root.right)
        else:
            return 2 ** (h-1) + self.countNodes(root.left) 
            
    def countWorker(self, node, count):
        
        if node.left is None and node.right is None:
        #    count += 1
            return count
        else:
            if node.left is not None:
                count += 1
                count = self.countWorker(node.left, count)
            if node.right is not None:
                count += 1
                count = self.countWorker(node.right, count)
        return count

if __name__ == '__main__':
    s = Solution()
    
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    print s.countNodes(t1)
    
    
    