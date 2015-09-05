'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#        profit = 0
#        if not prices:
#            return profit
#        
#        days_len = len(prices)
#        b_price = None     
#        b_day = 0
#        
#        while not b_price or prices[b_day] < b_price:
#            b_price = prices[b_day]
#            last_price = None
#            next_chance = None
#            for j in xrange(b_day+1, days_len):
#                #find the next lowest point
#                if not next_chance:
#                    if last_price is not None and prices[j] > last_price:
#                        next_chance = j-1
#                    last_price = prices[j] 
#                
#                if prices[j] > b_price:         
#                    if prices[j] - b_price > profit:
#                        profit = prices[j] - b_price
#            if next_chance is None:
#                break
#            b_day = next_chance
#            
#        return profit
        '''
         the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array, 
         and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.
        '''
        
        profit = 0
        if not prices:
            return profit
        
        days_len = len(prices)
        cur = 0
        for i in xrange(1, days_len):
            tmp = prices[i] - prices[i-1]
            cur = cur + tmp if cur > 0 else tmp 
            profit = profit if profit > cur else cur
        return profit
        
if __name__ == '__main__':
    
    test = [3,3,5,0,0,3,1,4]

    s = Solution()
    print s.maxProfit(test)
    
    pass 