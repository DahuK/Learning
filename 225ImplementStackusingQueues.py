'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
'''

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q = []
        self.q2 = []
        
    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q.append(x)

    # @return nothing
    def pop(self):
        while self.q:
            tmp = self.q.pop(0)
            if self.q:
                self.q2.append(tmp)
        self.q = self.q2
        self.q2 = []
        
    # @return an integer
    def top(self):
        while self.q:
            tmp = self.q.pop(0)
            self.q2.append(tmp)
        self.q = self.q2
        self.q2 = []
        return tmp

    # @return an boolean
    def empty(self):
        if not self.q:
            return True
        return False
        
if __name__ == '__main__':
    s = Stack() 
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.pop()
    print s.top()
    s.pop()
    s.pop()
    print s.top()
    print s.empty()