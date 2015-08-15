class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.child = {}
        self.is_end = False
        
class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    
    def __init__(self):
        self.root = TrieNode()
        self.result = []
        
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        current = self.root
        for letter in word:
            current.child[letter] = current.child.get(letter, TrieNode())
            current = current.child[letter]
        current.is_end = True
    
    def dfs(self, node, board, i, j, word=''):
        if node.is_end:
            self.result.append(word)
            node.is_end = False
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            char = board[i][j]
            child = node.child.get(char)
            if child is not None:
                word = word + char
                board[i][j] = None
                self.dfs(child, board, i+1, j, word)
                self.dfs(child, board, i, j+1, word)
                self.dfs(child, board, i-1, j, word)
                self.dfs(child, board, i, j-1, word)     
                board[i][j] = char
                
    def findWords(self, board, words):
        if board is None:
            return None
        
        for word in words:
            self.insert(word)
            
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(self.root, board, i, j)
        return self.result
                
        
if __name__ == '__main__':
    pass