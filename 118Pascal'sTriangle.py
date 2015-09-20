'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        last_row = [1]
        res = [last_row]
        for r in xrange(1,numRows):
            
            cur_row = [1]
            for i in xrange(1, len(last_row)):
                cur_row.append(last_row[i-1] + last_row[i])
            cur_row.append(1)
            last_row = cur_row
            res.append(cur_row)
        return res
        
if __name__ == '__main__':
    s = Solution()
    print s.generate(5)