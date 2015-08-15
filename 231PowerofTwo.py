'''
Given an integer, write a function to determine if it is a power of two.
'''

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False 
        while True:
            if n<=2:
                return True
            
            if n%2 == 1:
                return False
            n = n/2
        return False
        
if __name__ == '__main__':
    
    s = Solution()
    n = 1
    print s.isPowerOfTwo(n)
    n = 1024
    print s.isPowerOfTwo(n)
    pass