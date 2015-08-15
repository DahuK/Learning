'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        
        o_stack = []
        marked = [[False for i in board[0]] for j in board]
        
        for row in xrange(len(board)):
            for col in xrange(len(board[0])):
                if board[row][col] is 'O' and not marked[row][col]:
                    is_open = []
                    self.bfs( board, row, col, is_open, o_stack)
                    while o_stack:
                        position = o_stack.pop()
                        if not is_open: 
                            board[position[0]][position[1]] = 'X'
                        marked[position[0]][position[1]] = True
                        
    def bfs(self, board, row, col, is_open, o_stack):
        
        if board[row][col] == 'O':
            if row == 0 or col == 0 or row==len(board)-1 or col==len(board[0])-1 :
                #it is an open range, would not change
                is_open.append('T')
            position = [row, col]
            o_stack.append(position)
        if not row==len(board)-1 and  board[row+1][col] == 'O':
            self.bfs(board, row+1, col, is_open, o_stack)
        if not col==len(board[0])-1 and board[row][col+1] == 'O':
            self.bfs(board, row, col+1, is_open, o_stack)
            
if __name__ == '__main__':
    
#    x = [[0 for i in xrange(3)] for j in xrange(4)]
#    print x
#    
#    r = [[False for i in x] for j in x[0]]
#    print r 
#    
    s = Solution()
    test = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X'] ]
    test = [['X', 'X', 'X'], ['X', 'O', 'X'], ['X', 'X', 'X']]
    s.solve(test)
    print test
    pass