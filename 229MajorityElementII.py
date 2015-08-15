'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        
        cand, cand1, count, count1 = 0,1,0,0
        for n in nums:
            if n==cand:
                count +=1
            elif n==cand1:
                count1+=1
            elif count==0:
                cand = n
                count = 1
            elif count1==0:
                cand1 = n
                count1 = 1
            else:
                count-=1
                count1-=1
        
        return [n for n in [cand, cand1] if nums.count(n) > len(nums)//3]
        
        
if __name__ == '__main__':
    
    s = Solution()
    nums = [1]
    print s.majorityElement(nums)
    pass