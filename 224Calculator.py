'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces.

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
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
        for x in s:
            if x.isdigit():
                if not has_digit:
                    has_digit = True
                    ops_index = int_index
            else:          
                
                if has_digit:
                    num_stack.append(int(s[ops_index : int_index]))
                    has_digit = False
                if x == ' ':
                    int_index += 1
                    continue
                if x == ')':
                    tmp_ops = []
                    tmp_num = []
                    while True:
                        ops = ops_stack.pop()
                        num = num_stack.pop()
                        if ops is '(':
                            while True:
                                if not tmp_ops:
                                    break
                                num = self.calc(tmp_ops.pop(), num, tmp_num.pop())
                            num_stack.append(num)
                            break
                        tmp_num.append(num)
                        tmp_ops.append(ops)                       
                else:
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
                     '-' :lambda: self.sub(x,y)}
        return calculation[ops]()

    def add(self, a, b): 
        return a + b

    def sub(self, a, b): 
        return a - b
        
if __name__ == '__main__':
    s = Solution()
    test = "   (  3 ) "
        
    res = s.calculate(test)
    print res
    