'''
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
'''
import copy

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]
    
        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]
    
        return max(merge(prep(nums1, i), prep(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))
    
#         if nums1 is None or nums2 is None:
#             return None
#         m = len(nums1)
#         n = len(nums2)
#         
#         if k > m + n:
#             return None
#         res = []
#         self.max_nums = [0 for i in xrange(k)]
#         self.findingMax(res, nums1, nums2, k, self.max_nums)
#         return self.max_nums
        
    def findingMax(self, res, nums1, nums2, left, max_nums):
        max_num1 = max_num2 = -1
        index_num1 = index_num2 = 0
        l1 = len(nums1)
        l2 = len(nums2) 
        if l1 > 0:
            dis1 = l1 - left + l2 + 1
            dis1 = dis1 if l1 > dis1 else l1
            for i in xrange(dis1):
                if nums1[i] > max_num1:
                    max_num1 = nums1[i]
                    index_num1 = i
                
        if l2 > 0:
            dis2 = l2 - left + l1 + 1
            dis2 = dis2 if l2 > dis2 else l2
            for i in xrange(dis2):
                if nums2[i] > max_num2:
                    max_num2 = nums2[i]
                    index_num2 = i
                
        max_num = max(max_num1, max_num2)
        res.append(max_num)
        left = left - 1
        if left == 0:
            if res == max(self.max_nums, res):
                self.max_nums = res
            return
        if max_num1 == max_num2:
            res_copy = copy.deepcopy(res)
            self.findingMax(res, nums1[index_num1 + 1:], nums2, left, self.max_nums)
            self.findingMax(res_copy, nums1, nums2[index_num2 + 1:], left, self.max_nums)
        else:
            if max_num == max_num1:
                self.findingMax(res, nums1[index_num1 + 1:], nums2, left, max_nums)
            else:
                self.findingMax(res, nums1, nums2[index_num2 + 1:], left, max_nums)
                
if __name__ == '__main__':
    for i in xrange(1,5):
        print i
    def merge(a, b):
        return [max(a, b).pop(0) for _ in a+b]
    
    def prep(nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]
    nums1 = [6, 7]
    nums2 = [9, 1, 2, 5, 8, 3]
    print prep(nums2, 5)
    
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    
    nums1 = [3, 9]
    nums2 = [8, 9]
    k = 3
    
    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5
    
    nums1 = [6, 7]
    nums2 = [6, 0, 4]
    k = 5
    
    nums1 = [6,4,7,8,6,5,5,3,1,7,4,9,9,5,9,6,1,7,1,3,6,3,0,8,2,1,8,0,0,7,3,9,3,1,3,7,5,9,4,3,5,8,1,9,5,6,5,7,8,6,6,2,0,9,7,1,2,1,7,0,6,8,5,8,1,6,1,5,8,4]
    nums2 = [3,0,0,1,4,3,4,0,8,5,9,1,5,9,4,4,4,8,0,5,5,8,4,9,8,3,1,3,4,8,9,4,9,9,6,6,2,8,9,0,8,0,0,0,1,4,8,9,7,6,2,1,8,7,0,6,4,1,8,1,3,2,4,5,7,7,0,4,8,4]
    k = 70

    s = Solution()
    print s.maxNumber(nums1, nums2, k)
    pass
