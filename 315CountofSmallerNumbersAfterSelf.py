'''

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

Created on Feb 15, 2016

@author: Dahu
'''

class Solution(object):
    
    def getSum(self, T, idx):
        val = 0
        while idx:
            val += T[idx]
            idx -= idx & (-idx)
        return val
    
    def update(self, T, idx, val):
        while idx <= len(T)-1:
            T[idx] += val
            idx += idx & (-idx) 
        
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if nums is None:
            return None
        if len(nums) == 0:
            return []
        
        min_val = min(nums)
        if min_val <= 0 :
            nums = [a + 1 - min_val for a in nums]
        T = [0] * (max(nums) + 1)
        res = []
        
        for num in nums[::-1]:
            res.append(self.getSum(T, num-1))
            self.update(T, num, 1)
        return res[::-1]
        
if __name__ == '__main__':
    s = Solution()
    nums = [5, 2, 6, 1]
    print s.countSmaller(nums)
    pass