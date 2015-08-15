'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
'''


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        if k < 0:
            return 
        if k > len(nums):
            k = k % len(nums) 
        back_nums = nums[:-k]
        front_nums = nums[-k:]
        res = front_nums + back_nums
        for r in xrange(len(res)):
            nums[r] = res[r]
        
if __name__ == '__main__':
    test = [1,2,3]
    print test[:-4]
    s = Solution()
    s.rotate(test, 4)
    print test
    