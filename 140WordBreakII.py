'''
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
'''

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        
        if s is None or wordDict is None:
            return None
        sol = []
        
#        s_set = set(s)
#        d_set = set()
#        for d in wordDict:
#            if not d in s:
#                return sol
#            d_set |= set(d)
#        
#        if s_set > d_set:
#            return sol 
        
        #check the s first
        n = len(s)
        can_find = [False] * n
        for i in xrange(n):
            for j in xrange(i+1, n+1):
                if not s[i:j] in wordDict:
                    continue
                if i==0 or (can_find[i-1] and i>0):
                    print str(i) + ' ' + str(j)  + ' ' + s[i:j]
                    can_find[j-1] = True
        if not can_find[-1]:
            return sol
        
        sol = self.findWord(s, wordDict, None, sol)
        return sol
        
    def findWord(self, left_s, wordDict, words, sol):
        for i in xrange(len(left_s)):       
            w = left_s[:i+1]
            if w in wordDict:
                new_words = w if words is None else words + ' ' + w    
                new_left_s = left_s[i+1:]
                if len(new_left_s) is 0:
                    sol.append(new_words)
                    return sol
                self.findWord(new_left_s, wordDict, new_words, sol)

        return sol
        
if __name__ == '__main__':
    
#    ls = 'asdasd'
#    n = len(ls)
#    for i in xrange(n):
#        for j in xrange(i+1, n+1):
#            print ls[i:j]
#    t = set("Hello")  
#    print t
    
    ss = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
#    ss = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
#    dict = ["a","aa","ba"]
    s = Solution()
    print s.wordBreak(ss, dict)