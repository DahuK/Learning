'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Could you solve it in linear time?
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        max_win = []
        if nums == []:
            return max_win
        queue = []
        max_index = 0
        max_v = nums[0]
        for i in xrange(k):          
            if nums[i] >= max_v:
                max_v = nums[i]
                max_index = i
            queue.append(nums[i])
        max_win.append(max_v)
        for i in xrange(k, len(nums)):
            queue.pop(0)
            queue.append(nums[i])
            if max_index == i-k:
                #max has been poped
                max_index+=1
                max_v = nums[max_index]
                step = 0
                for j in xrange(1, len(queue)):
                    if queue[j] >= max_v:
                        max_v = queue[j]
                        step = j
                max_index += step
            if nums[i] > max_v:
                max_v = nums[i]
                max_index = i
            max_win.append(max_v)
        return max_win
    
if __name__ == '__main__':
#    nums = [1,5,3,10,4,12]
#    
#    for i in xrange(3, len(nums)):
#        print i
#    print nums[3:]
#    #nums = []
    
    test = [-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7]
    s = Solution()
    k = 7
    print s.maxSlidingWindow(test, k)
    