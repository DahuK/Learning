class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums is None: 
            return None
        number = len(nums)
        max_array = []
        for index in xrange(number):
            if index==0:
                max_array.append(nums[0])
            elif index==1:
                max_array.append(max(nums[0], nums[1]))
            else:
                max_rob = max(max_array[index-1], max_array[index-2]+ nums[index])
                max_array.append(max_rob)
        if len(max_array) == 0:
            return 0
        return max_array.pop()
        
    def test(self, kk):
        kk.append('X')

if __name__ == '__main__':
    nums = [1,5,3,10,4,12]
    #nums = []
    s = Solution()
    print s.rob(nums)
    
    kk = []
    s.test(kk)
    print kk