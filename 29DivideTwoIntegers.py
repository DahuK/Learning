'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        res = 0
        if divisor is 0 or dividend==-2147483648 and divisor is -1:
            return 2147483647
        sign = -1 if ( (dividend < 0) != (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor :
            factor = 1
            tmp = divisor
            while True: 
                if dividend - (tmp << 1) < 0:
                    break
                tmp = tmp << 1
                factor = factor << 1
            dividend-=tmp
            res+=factor
        return res * sign
         
if __name__ == '__main__':
    dividend = 16
    divisor = 3
   # print ( (dividend < 0) != (divisor < 0) )
    s = Solution()
    print s.divide(dividend, divisor)
    
    pass