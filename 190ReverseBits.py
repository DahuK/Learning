'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), 
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        i = 0
        sum = 0        
        while i < 32:   
            sum += (((n>>i) << 31)%4294967296)>>i
            i +=1 
        return sum
        
if __name__ == '__main__':
    
    tt = 43261596
    print tt>>2
    print tt<<2
    
    s = Solution()
    print s.reverseBits(tt)
    
    pass