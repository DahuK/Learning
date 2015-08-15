'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        
        output = []
        if k < 1 or n < 1:
            return output
        for i in xrange(9):
            res = [i+1]
            if k == 1:
                if n == i+1:
                    output.append([i+1]) 
            else:
                self.combine(output, res, i+2, n-i-1, k-1)

        return output
    
    def combine(self, output, res, value, left_n, left_k):
        if left_n < value * left_k:
            return
        if left_k == 1:
            if left_n < 10:
                res.append(left_n)
                output.append(res)
            return
        while True:
            if left_n <= value*left_k or value > 10-left_k:
                return
            next_res = list(res)
            next_res.append(value)
            value +=1
            self.combine(output, next_res, value, left_n-value+1, left_k-1)
               
        
if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(4, 24)
    pass