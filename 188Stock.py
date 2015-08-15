class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        ll = len(prices)
        #corner process
        if(k > ll / 2): 
            return self.quickMaxProfit(prices)
        
        pp = [[0 for col in range(ll)] for row in range(k+1)]
        h = 1
        while h <= k:
            tmpMoney = pp[h-1][0] - prices[0]  #initialize the money with first buy
            for l in xrange(ll-1):
                pp[h][l+1] = pp[h][l] if pp[h][l] > tmpMoney + prices[l+1] else tmpMoney + prices[l+1]
                tmpMoney = tmpMoney if tmpMoney >= pp[h-1][l] - prices[l+1] else pp[h-1][l] - prices[l+1]
            h = h+1
        return pp[k][ll-1]

    def quickMaxProfit(self, prices):
        profit = 0
        for x in xrange(len(prices) -1):
            if prices[x+1] > prices[x]:
                profit += prices[x+1] - prices[x]
        return profit
            
if __name__ == '__main__':
    if 2>=1:
        print 'adsas'
    s = [1,3,2]
    for x in xrange(0):
        print x
    
    k =1 
    pp = [[0 for col in range(len(s))] for row in range(k)]
    print pp
    #0, [1,3]
    s = Solution()
    prices = [1,3]
    print s.maxProfit(0, prices)
    
    