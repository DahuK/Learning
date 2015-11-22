'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
import collections
import string

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        
        queue = collections.deque([(beginWord, 1)])
        ls = string.ascii_lowercase
        visited = set()
        while queue:
            
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            
            for i in xrange(len(word)):
                for j in ls:
                    if j is not word[i]:
                        next_w = word[:i] + j + word[i+1:]
                        if next_w in wordList and next_w not in visited:
                            queue.append((next_w, dist+1))
                            visited.add(next_w)
        return 0
                                 
        
if __name__ == '__main__':
    tt = ['a','b','v']
    print tt.pop(0)
    
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    
    s = Solution()
    print s.ladderLength(beginWord, endWord, wordList)
    pass