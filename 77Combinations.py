'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
#        res = []
#        if k > n:
#            return res
#        if k is 1:
#            for i in xrange(1, n+1):
#                res.append([i])
#            return res
#        
#        end_index = n - k + 2
#        for i in xrange(1, end_index): 
#            for j in xrange(i+1, end_index + 1):
#                r = [i]
#                num = j
#                for z in xrange(k-1):
#                    r.append(num)
#                    num = num + 1
#                res.append(r)
#        return res
        
        res = []
        if k > n:
            return res
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l==k:
                res.append(stack[:])
            if l==k or x > n-k+l+1:
                if not stack:
                    return res
                x = stack.pop() + 1
            else:
                stack.append(x)
                x = x+1
        return res
              
if __name__ == '__main__':
    s = Solution()
    n = 2
    k = 1
    print s.combine(n, k)
    pass