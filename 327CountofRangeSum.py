'''

'''

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
        sm = [0]
        for n in xrange(len(nums)):
            sm.append(sm[-1] + nums[n]) 
            
        def sort(start, end):
            mid = (start + end)/2
            if start==mid:
                return 0
            count = sort(start, mid) + sort(mid, end)
            j = k = mid
            for left in sm[start: mid]:
                while j < end and sm[j] - left < lower: j+=1
                while k < end and sm[k] - left <= upper: k+=1
                count += k-j
            sm[start: end] = sorted(sm[start: end])
            return count
        return sort(0, len(sm))
        
if __name__ == '__main__':
    test = [2147483647,-2147483648,-1,0]
    s = Solution()
    print s.countRangeSum(test, -1, 0)
    
    