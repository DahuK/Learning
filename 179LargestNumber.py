
#Given a list of non negative integers, arrange them such that they form the largest number.
#
#For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
#Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        if len(num) == 1:
            return str(num[0])
        order_list = []
        for n in num:
            sn = str(n)
            index = 0
            for o in order_list:
                if self.compare(sn, o):
                    order_list.insert(index, sn)
                    break
                else:
                    index+=1
            if index == len(order_list):
                order_list.append(sn)
        
        result = ''.join(order_list)
        if result[0] == '0':
            return '0'
        else:
            return ''.join(order_list)

    def compare(self, num, target):
        return True if num + target > target + num else False
    
    
#    def processNumber(self, num):
#        dl = []
#        while True:
#            t = num % 10
#            num = num / 10
#            dl.insert(0, t)
#            if num == 0: 
#                break
#        return dl
#    
#    
#    def compare(self, num_list, target_list):
#        nl = len(num_list)
#        tl = len(target_list)
#        ll = nl if nl <= tl else tl
#        for i in xrange(ll):
#            if num_list[i] > target_list[i]:
#                return True
#            elif num_list[i] < target_list[i]:
#                return False
#            
#        if nl == tl: 
#            return False
#        left_list = target_list[ll:] if nl < tl else num_list[ll:]
#        for ln in left_list:
#            if ln > 
#        
#        return False if ll == tl else True
    
if __name__ == '__main__':
    a = '1231231'
    b = '1312111'
    
    if a > b:
        print 'aaaa'
    else:
        print 'bbbb'
    
    
    a = [1,2,4,3,2]
    b = map(str, a)
    print ''.join(b)
    
    s = Solution()
    a = [3, 30, 34, 5, 9]
    a = [0,0]
    print s.largestNumber(a)
    
    
    
        