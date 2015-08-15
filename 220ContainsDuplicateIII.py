'''
Given an array of integers, find out whether there are two distinct indices i and j in the array
 such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
'''


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        #bucketing
        if k < 1 or t < 0:
            return False
        data_map = {}
        for i in xrange(len(nums)):
            data = nums[i]/(t+1)
            for key in [data-1, data, data+1]: 
                if key in data_map and abs(data_map[key]- nums[i]) <= t:
                    return True
            if len(data_map) >= k:
                data_map.pop(nums[i-k]/(t+1))
            data_map[data] = nums[i]

        return False
        

if __name__ == '__main__':
#    nums = [1,2,3]
#    for i in xrange(len(nums)):
#        print i
#    print -2/1
    s = Solution()
    nums = [0]
    nums = [1,2]
    k = 0
    t = 1
    print s.containsNearbyAlmostDuplicate(nums, k, t)
    pass