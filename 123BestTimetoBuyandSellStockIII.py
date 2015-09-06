'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        days_len = len(prices)
        if prices is None or days_len is 0 or days_len is 1:
            return profit
        
        profit = [0 for i in xrange(days_len)]
        profit_post = [0 for i in xrange(days_len)]
        j = days_len - 2
        min_profit = prices[0]
        max_profit_post = prices[days_len-1]
        for i in xrange(1, days_len):
            profit[i] = max(profit[i-1], prices[i] - min_profit)
            min_profit = min(min_profit, prices[i])
            profit_post[j] = max(profit_post[j+1], max_profit_post - prices[j])
            max_profit_post = max(max_profit_post, prices[j])
            j = j-1
        #join the two part of transactions
        sum_profix = 0
        for i in xrange(1, days_len):
            sum_profix = max(sum_profix, profit[i] + profit_post[i])
        return sum_profix
        
if __name__ == '__main__':
    test = [3,3,5,0,0,3,1,4]
    #test = [1,2]
    s = Solution()
    print s.maxProfit(test)
    
    pass 