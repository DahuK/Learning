'''
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return None
        last_row = [1]
        
        for r in xrange(rowIndex):
            cur_row = [1]
            for i in xrange(1, len(last_row)):
                cur_row.append(last_row[i-1] + last_row[i])
            cur_row.append(1)
            last_row = cur_row
        return last_row

if __name__ == '__main__':
    s = Solution()
    print s.getRow(3)