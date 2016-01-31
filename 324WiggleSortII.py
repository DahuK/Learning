'''
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

1, 5, 3,2,7
1 2 3 5 7

3 7 2 5 1
2 3 1 5 7
3 5 2 7 1

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) is 0:
            return
        sort_nums = sorted(nums)
        l = len(sort_nums)
        mid = l / 2 + l % 2 
    
        for i in xrange(mid - 1):
            nums[i * 2] = sort_nums[mid - 1 - i]
            nums[i * 2 + 1] = sort_nums[-i-1]
        
        if l % 2 is 0: 
            nums[-1] = sort_nums[mid]
            nums[-2] = sort_nums[0]
        else:
            nums[-1] = sort_nums[0] 
            
if __name__ == '__main__':
    
    ff = [1,4,6,7]
    for i in xrange(len(ff)):
        print ff.pop()
    print ff
    
    test = [1, 5, 1, 1, 6, 4]
#    test = [1, 3, 2, 2, 3, 1]
    s = Solution()
    s.wiggleSort(test)
    print test
    pass
