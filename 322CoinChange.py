'''
Created on Jan 25, 2016

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.

@author: Dahu
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0
        
        coins = sorted(coins, reverse=True)
        upper_bound = (amount + coins[-1] - 1) / coins[-1] + 1  # +1!!
        
        self.res_size = upper_bound
        self.cal_size(coins, amount, 0)
        if self.res_size == upper_bound:
            return -1
        else:
            return self.res_size
        
    def cal_size(self, coins, amount, cur_size):
        #different denominations
        lower_bound = cur_size + (amount + coins[0] - 1) / coins[0]
        
        if lower_bound > self.res_size:
            return
        
        if len(coins) == 0:
            return
        
        #find a better solution
        if amount == coins[0] and cur_size + 1 < self.res_size:
            self.res_size = cur_size + 1
            return
        
        #first try the biggest solution
        if amount > coins[0]:
            self.cal_size(coins, amount - coins[0], cur_size + 1)
        #recursive try the other solution
        if len(coins) > 1:
            self.cal_size(coins[1:], amount, cur_size)
            
#         coins = sorted(coins)
#         res = []
#         def find_num(coins, left, res):
#             for c in xrange(1, len(coins) + 1):
#                 coin = coins[-c]
#                 if coin == left:
#                     # find a result
#                     res.append(coin)
#                     #print res
#                     return res
#                 elif coin < left:
#                     res.append(coin)
#                     find_num(coins, left - coin, res)
#                     
#         find_num(coins, amount, res)
#         return res
        
if __name__ == '__main__':
#     for i in xrange(3,0,-1):
#         print i
    print [0 for i in xrange(5)]
    t1 = [1,3,4]
    t2 = [1,4,5]
    if t1 == max([1,3,4], [1,4,5]):
        print 'LLLLLLLLL'
    tt = [1,3,4,5]
    print tt[:-1]
    s = set()
    s.add('asd')
    s.add('aass')
    for a in s:
        print a
    coins = [1, 3, 5]
    amount = 4
    s = Solution()
    print s.coinChange(coins, amount)
    pass
