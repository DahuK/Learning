'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None:
            return 0
        res = [[0 for i in xrange(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(0, len(triangle[i])):
                
                if j is 0:
                    res[i][j] = res[i-1][j] + triangle[i][j]
                elif j is len(triangle[i]) -1:
                    res[i][j] = res[i-1][j-1] + triangle[i][j]        
                else:
                    res[i][j] = min(res[i-1][j-1], res[i-1][j]) + triangle[i][j]
        return min(res[-1])
        
#    def _trace(self, triangle, last_index, min_sum, cur_sum, level): 
#        ll = triangle[level]
#        level = level + 1
#        for i in xrange(2):
#            index = last_index + i
#            val = ll[index]
#            new_sum = cur_sum + val
#            
#            if level == len(triangle):
#                min_sum = min(min_sum, new_sum)
#                print min_sum
#                return min_sum
#            else:
#                self._trace(triangle, index, min_sum, new_sum, level)
        
        
        
if __name__ == '__main__':
    test = [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    

    s = Solution()
    print s.minimumTotal(test)
    