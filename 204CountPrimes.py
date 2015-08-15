'''
Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n==0:
            return 0
        isPrime = [True for i in xrange(n)]
        isPrime[0] = False
        
        i = 2
        while i**2 < n:
            if not isPrime[i-1]:
                i+=1 
                continue
            j = i**2
            while j< n:
                isPrime[j-1] = False
                j+=i
            i+=1            
        
#        for i in xrange(2, int(n**0.5)):8
#            if not isPrime[i]: 
#                continue
#            for j in xrange(i**2, n, i):
#                isPrime[j] = False
        
        count = 0
        for i in xrange(n-1):
            if isPrime[i]:
                count+=1
        return count
        
        

if __name__ == '__main__':

    #print int(8**0.5)
    s = Solution()
    test = 2
    print s.countPrimes(test)
    
    pass