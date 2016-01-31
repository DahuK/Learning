'''
Created on Jan 31, 2016

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.

@author: Dahu
'''

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n > 0:
            return 0
        
        return int(n**(0.5))
#         counter = [0 for i in xrange(n)]
#         for i in xrange(1, n+1):
#             for j in xrange(i-1, n, i):
#                 counter[j] = 1 if counter[j] == 0 else 0
#         count = 0
#         for i in counter:
#             if i == 1:
#                 count += 1
#         return count
        
if __name__ == '__main__':
    
    s = Solution()
    print s.bulbSwitch(4)
    pass