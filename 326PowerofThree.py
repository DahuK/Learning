'''
Created on Jan 24, 2016

@author: Dahu
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n is 0:
            return False
        while n is not 1:
            if n % 3 is not 0:
                return False
            n = n / 3
        return True
        
if __name__ == '__main__':
    for i in xrange(3):
        print i
    
    s = Solution()
#     print s.isPowerOfThree(5)
#     print s.isPowerOfThree(18)
#     print s.isPowerOfThree(27)
#     print s.isPowerOfThree(3)
    print s.isPowerOfThree(1)