'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

hint

The key is to use the fact that the lower bound of the gap is (maxV - minV )/ (sSize - 1). With such in mind, we can put all the num elements into different bucket with 
size (maxV - minV )/ (sSize - 1) (please note when such size is less than 1, then use 1 instead) and in such way,
 we only need to consider the min and max of each bucket and don't need to worry the numbers in between of each bucket since the gaps among those elements 
 are smaller than the bucket size, and then the lower bound of the gap, so they can not achieve the max gap.

class Solution { public: int maximumGap(vector &num) { int sSize = num.size(); int i, res =0; int minV, maxV; int bucketsize, bucketnum, bucketid; int maxGap = INTMIN; int last_max;
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maximumGap(self, nums):
        size = len(nums)
        if size < 2:
            return 0
        
        max_num = max(nums)
        min_num = min(nums)
        bucket_size = (max_num - min_num)/(size-1)
        if bucket_size < 1:
            bucket_size = 1
        
        container = [set() for i in xrange(size)]
        for n in nums:
            n_b = min((n - min_num)/bucket_size, size-1)
            container[n_b].add(n)
        
        max_gap = last = 0
        for c in xrange(len(container)):
            if len(container[c]):
                max_gap = max(max_gap, min(container[c])- max(container[last]))
                last = c
        return max_gap
    
if __name__ == '__main__':
    
#    test = [1,2,3]
#    tt = set()
#    x = [set() for i in xrange(4)]
#    print x
    
    test = [3,6,9,1]
    s = Solution()
    
    print s.maximumGap(test)
    
    pass