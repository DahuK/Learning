'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.minlist = []
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
#        end = len(self.minlist) -1 
#        push_index = self.find_index(self.minlist, 0, end, x)
#        self.minlist.insert(push_index, x)
        self.stack.append(x)
        if x <= self.getMin():
            self.minlist.append(x)

    # @return nothing
    def pop(self):
#        x = self.stack.pop()
#        end = len(self.minlist) -1 
#        pop_index = self.find_index(self.minlist, 0, end, x)
#        del self.minlist[pop_index]
        end = len(self.stack) -1
        if(self.stack[end] == self.getMin()):
            self.minlist.pop()
        self.stack.pop()

    # @return an integer
    def top(self):
        top_index = len(self.stack) -1 
        return self.stack[top_index]

    # @return an integer
    def getMin(self):
#        #min_index = len(self.minlist) -1 
#        return self.minlist[0]
        if len(self.minlist) == 0: 
            return 2147483647
        min_index = len(self.minlist) -1 
        return self.minlist[min_index]
        
        
    def find_index(self, minlist, begin, end, x):
        if end == -1:
            return 0
            
        while True:
            if begin + 1 ==end or begin==end:
                if x < minlist[begin]:
                    return begin
                if x > minlist[end]:
                    return end + 1
                else:
                    return begin + 1
            
            index = (begin + end)/2
            if minlist[index] < x:         
                begin = index
            else:
                end = index
            self.find_index(minlist, begin, end, x)        
    
if __name__ == '__main__':
    
    a = [2,3,6]
#    a.insert(2, 8)
#    print a
    m = MinStack()
    tt = 3
#    index =  m.find_index(a, 0, len(a) -1, tt) 
#    print index
#    a.insert(index, tt)
#    print a

#push(2147483646),push(2147483646),push(2147483647),top,pop,getMin,
#pop,getMin,pop,push(2147483647),top,getMin,push(-2147483648),top,getMin,pop,getMin
    m.push(2147483646)
    m.push(2147483646)
    m.push(2147483647)
    print m.top()
    print m.top()
    print m.getMin()
    m.pop()
    print m.getMin()
    m.pop()
    m.push(2147483647)
    print m.top()
    print m.getMin()
    m.push(-2147483648)
    print m.top()
    print m.getMin()
    m.pop()
    print m.getMin()
    
    
#    print m.stack
#    print m.getMin()
#    print m.top()
#    print m.stack
#    m.pop()
#    print m.getMin()
#    print m.stack
    
    pass