'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        if prices is None:
            return profit
        day_len = len(prices)
        for i in xrange(1, day_len):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit = profit + tmp
        return profit
        
if __name__ == '__main__':
    test = [3,3,5,0,0,3,1,4]

    s = Solution()
    print s.maxProfit(test)
    
    pass 