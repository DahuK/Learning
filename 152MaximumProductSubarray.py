'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        
        res = last_max = last_min = nums[0]
        
        for i in xrange(1, len(nums)):
            c_max = max(nums[i], nums[i]*last_max, nums[i]*last_min)
            last_min = min(nums[i], nums[i]*last_max, nums[i]*last_min)
            res = max(res, c_max)
            last_max = c_max
        return res
        
if __name__ == '__main__':
    s = Solution()
    test = [2,4,-1,-10]
    
    res = s.maxProduct(test)
    print res