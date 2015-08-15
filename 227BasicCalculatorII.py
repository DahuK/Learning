'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''


class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        ops_stack = []
        num_stack = []
        int_index = 0
        ops_index = 0
        has_digit = False
        higher_cal = None
        for x in s:
            if x.isdigit():
                if not has_digit:
                    has_digit = True
                    ops_index = int_index
            else:          
                
                if has_digit:
                    num = int(s[ops_index : int_index])
                    if higher_cal:
                        num = self.calc(higher_cal, num_stack.pop(), num)
                        num_stack.append(num)
                    else:
                        num_stack.append(int(s[ops_index : int_index]))
                    has_digit = False
                if x == ' ':
                    int_index += 1
                    continue                          
                else:
                    if x == '*' or x == '/':
                        higher_cal = x
                    else:
                        higher_cal = None
                    ops_stack.append(x)
            int_index += 1
        if has_digit:
            num_stack.append(int(s[ops_index : int_index]))
        numa = num_stack.pop(0)
        while True:
            if not num_stack:
                break
            numb = num_stack.pop(0)
            ops = ops_stack.pop(0)
            numa = self.calc(ops, numa, numb)
        return numa
                    
    
    def calc(self, ops, x, y):
        calculation  = {'+' :lambda: self.add(x,y), 
                     '-' :lambda: self.sub(x,y),
                     '*' : lambda: self.multi(x,y),
                     '/' : lambda: self.div(x,y)}
        return calculation[ops]()

    def add(self, a, b): 
        return a + b

    def sub(self, a, b): 
        return a - b
   
    def multi(self, a, b): 
        return a * b
    
    def div(self, a, b): 
        return a / b 
if __name__ == '__main__':
    s = Solution()
    test = "3+2*2"
        
    res = s.calculate(test)
    print res