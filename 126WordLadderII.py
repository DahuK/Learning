'''
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''
import string
import copy

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        
        result = []
        neighbors = {}
        distance = {}
        solution = []
        
        wordlist.add(endWord)
        self.bfs(beginWord, endWord, wordlist, neighbors, distance)
        self.dfs(beginWord, endWord, wordlist, neighbors, distance, result, solution)
        return result
        
    def findNeighbors(self, word, wordlist):
        result = []
        ls = string.ascii_lowercase
        for i in xrange(len(word)):
            for j in ls:
                if j is not word[i]:
                    new_word = word[:i] + j + word[i+1:]
                    if new_word in wordlist:
                        result.append(new_word)
        return result
        
    def bfs(self, beginWord, endWord, wordlist, neighbors, distance):
        neighbors[beginWord] = []
        for wl in wordlist:
            neighbors[wl] = []
            
        queue = [beginWord]
        distance[beginWord] = 0
        while queue:
            find_end = False
            for i in xrange(len(queue)):
                cur_word = queue.pop(0)
                cur_dis = distance[cur_word]
                cur_ngbs = self.findNeighbors(cur_word, wordlist)
                
                for ngb in cur_ngbs:
                    neighbors[cur_word].append(ngb)
                    if ngb not in distance:
                        distance[ngb] = cur_dis + 1
                        if endWord == ngb:
                            find_end = True
                        else:
                            queue.append(ngb)
                
                if find_end:
                    break
                
        
    def dfs(self, curWord, endWord, wordlist, neighbors, distance, res, solution):
        solution.append(curWord)
        if endWord == curWord:
            res.append(copy.deepcopy(solution))
        else:
            for ngb in neighbors[curWord]:
                if distance[ngb] == distance[curWord]+1:
                    self.dfs(ngb, endWord, wordlist, neighbors, distance, res, solution)
        solution.pop()
  
if __name__ == '__main__':
    
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    s = Solution()
    
    print s.findLadders(beginWord, endWord, wordList)
    pass